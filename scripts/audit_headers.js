const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

function githubSlug(text) {
  return text
    .replace(/\r/g, '')
    .toLowerCase()
    .trim()
    // Remove markdown links like [text](url) -> text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    // Remove code ticks
    .replace(/`([^`]+)`/g, '$1')
    // In GFM, punctuation like . : ( ) / ? ! & * are removed
    .replace(/[^\p{L}\p{N}\s\-_]/gu, '')
    // Replace spaces with hyphens
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

function getAllFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (file !== 'node_modules' && file !== '.git') {
        getAllFiles(fullPath, fileList);
      }
    } else if (file.endsWith('.md')) {
      fileList.push(fullPath);
    }
  });
  return fileList;
}

const mdFiles = getAllFiles(docsDir);
const headerIssues = [];

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  const lines = content.split('\n');

  // Extract all headings
  const slugCounts = {};
  const slugs = new Set();
  const headings = [];

  lines.forEach((line, idx) => {
    const match = line.match(/^#{1,6}\s+(.+)$/);
    if (match) {
      const headingText = match[1].trim();
      let slug = githubSlug(headingText);
      if (slugCounts[slug] !== undefined) {
        slugCounts[slug]++;
        slug = `${slug}-${slugCounts[slug]}`;
      } else {
        slugCounts[slug] = 0;
      }
      slugs.add(slug);
      headings.push({ lineNum: idx + 1, text: headingText, slug });
    }
  });

  // Find all internal anchor links: [text](#anchor)
  const anchorRegex = /\[([^\]]+)\]\((#[^)]+)\)/g;
  let match;
  while ((match = anchorRegex.exec(content)) !== null) {
    const rawAnchor = match[2];
    const targetSlug = decodeURIComponent(rawAnchor.substring(1)).replace(/\r/g, '').trim();
    if (!slugs.has(targetSlug)) {
      headerIssues.push({
        file: relPath,
        linkText: match[1],
        targetAnchor: rawAnchor,
        targetSlug: targetSlug
      });
    }
  }
});

console.log('--- HEADER ANCHOR ISSUES FOUND ---');
console.log(JSON.stringify(headerIssues, null, 2));
