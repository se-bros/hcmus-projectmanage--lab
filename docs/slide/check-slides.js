const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const DIST_DIR = path.join(__dirname, 'dist');
const SCREENSHOT_DIR = path.join(__dirname, 'screenshots');
const PORT = 3099;

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

// Simple static server for dist folder
function createServer() {
  const mimeTypes = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2'
  };

  const server = http.createServer((req, res) => {
    let filePath = path.join(DIST_DIR, req.url.split('?')[0]);
    if (filePath.endsWith('/') || !path.extname(filePath)) {
      filePath = path.join(DIST_DIR, 'index.html');
    }

    fs.readFile(filePath, (err, content) => {
      if (err) {
        fs.readFile(path.join(DIST_DIR, 'index.html'), (err2, htmlContent) => {
          if (err2) {
            res.writeHead(404);
            res.end('Not Found');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(htmlContent);
          }
        });
      } else {
        const ext = path.extname(filePath).toLowerCase();
        const contentType = mimeTypes[ext] || 'application/octet-stream';
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
      }
    });
  });

  return new Promise((resolve) => {
    server.listen(PORT, () => {
      console.log(`Static server running on http://localhost:${PORT}`);
      resolve(server);
    });
  });
}

async function auditSlides() {
  const server = await createServer();
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();

  console.log('Navigating to Slidev app...');
  await page.goto(`http://localhost:${PORT}/1`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  // Find total slides dynamically
  const totalSlides = await page.evaluate(() => {
    if (window.__slidev__ && window.__slidev__.nav && window.__slidev__.nav.total) {
      return window.__slidev__.nav.total;
    }
    const els = document.querySelectorAll('*');
    for (const el of els) {
      if (el.innerText && el.innerText.includes(' / ')) {
        const match = el.innerText.match(/\d+\s*\/\s*(\d+)/);
        if (match) return parseInt(match[1], 10);
      }
    }
    return 64;
  });

  console.log(`Detected total slides: ${totalSlides}`);
  const report = [];

  for (let i = 1; i <= totalSlides; i++) {
    await page.goto(`http://localhost:${PORT}/${i}`, { waitUntil: 'networkidle' });
    await page.waitForTimeout(800);

    const shotPath = path.join(SCREENSHOT_DIR, `slide-${String(i).padStart(2, '0')}.png`);
    await page.screenshot({ path: shotPath, fullPage: false });

    // Audit Slide DOM
    const slideAudit = await page.evaluate((slideNum) => {
      const issues = [];
      const layout = document.querySelector('.slidev-layout') || document.body;

      // 1. Overflow check
      const isOverflowingY = layout.scrollHeight > layout.clientHeight + 10;
      const isOverflowingX = layout.scrollWidth > layout.clientWidth + 10;
      if (isOverflowingY) {
        issues.push({
          type: 'OVERFLOW_Y',
          detail: `Content vertically overflows slide bounds (scrollHeight: ${layout.scrollHeight}px vs height: ${layout.clientHeight}px)`
        });
      }
      if (isOverflowingX) {
        issues.push({
          type: 'OVERFLOW_X',
          detail: `Content horizontally overflows slide bounds (scrollWidth: ${layout.scrollWidth}px vs width: ${layout.clientWidth}px)`
        });
      }

      // 2. Unparsed markdown / template error check
      const textContent = layout.innerText || '';
      if (textContent.includes('{{') || textContent.includes('}}')) {
        issues.push({ type: 'UNPARSED_SYNTAX', detail: 'Found raw unparsed template braces {{ ... }}' });
      }
      if (textContent.includes('[object Object]')) {
        issues.push({ type: 'UNRENDERED_OBJECT', detail: 'Found unrendered [object Object]' });
      }
      if (textContent.includes('undefined')) {
        issues.push({ type: 'UNDEFINED_TEXT', detail: 'Found "undefined" string rendered on slide' });
      }

      // 3. Small font check (font-size < 9px)
      const allTextNodes = Array.from(layout.querySelectorAll('*')).filter(
        (el) => el.children.length === 0 && el.innerText && el.innerText.trim().length > 0
      );
      let tinyCount = 0;
      allTextNodes.forEach((el) => {
        const fs = parseFloat(window.getComputedStyle(el).fontSize);
        if (fs < 9) {
          tinyCount++;
        }
      });
      if (tinyCount > 0) {
        issues.push({
          type: 'SMALL_FONT',
          detail: `Found ${tinyCount} text elements with font-size < 9px (potentially unreadable)`
        });
      }

      // 4. Slide Title & Layout Balance Check
      const heading = layout.querySelector('h1, h2');
      const titleText = heading ? heading.innerText.trim() : 'NO_TITLE';

      return {
        slide: slideNum,
        title: titleText,
        isOverflowingY,
        isOverflowingX,
        issues
      };
    }, i);

    report.push(slideAudit);
    console.log(`Slide ${i}/${totalSlides}: "${slideAudit.title}" - ${slideAudit.issues.length} issue(s)`);
  }

  await browser.close();
  server.close();

  // Save JSON report
  fs.writeFileSync(
    path.join(SCREENSHOT_DIR, 'audit-report.json'),
    JSON.stringify(report, null, 2)
  );

  console.log('\n--- AUDIT SUMMARY ---');
  let totalIssues = 0;
  report.forEach((r) => {
    if (r.issues.length > 0) {
      console.log(`\n🔴 Slide ${r.slide} [${r.title}]:`);
      r.issues.forEach((iss) => {
        console.log(`  - [${iss.type}] ${iss.detail}`);
        totalIssues++;
      });
    }
  });

  if (totalIssues === 0) {
    console.log('\n✅ ALL SLIDES PASSED! No overflow, unparsed markdown, small font, or visual rendering errors detected.');
  } else {
    console.log(`\n⚠️ Found ${totalIssues} potential visual/layout issues across slides.`);
  }
}

auditSlides().catch((err) => {
  console.error('Audit failed:', err);
  process.exit(1);
});
