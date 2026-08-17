const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

// Standard GFM slugger used by VS Code and GitHub
function toGfmSlug(text) {
  return text
    .toLowerCase()
    .trim()
    // Remove inline links [text](url) -> text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    // Remove code ticks
    .replace(/`([^`]+)`/g, '$1')
    // Remove HTML tags
    .replace(/<[^>]+>/g, '')
    // In GFM, all characters that are punctuation (including . , : / \ ( ) ? ! " ' “ ” & etc.) are removed except hyphens and underscores
    .replace(/[^\p{L}\p{N}\s\-_]/gu, '')
    // Replace whitespace with single hyphen
    .replace(/\s+/g, '-')
    // Replace multiple hyphens with single hyphen
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

console.log('--- REGENERATING TOCS AND FIXING ANCHORS ---');

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  let content = fs.readFileSync(file, 'utf8');

  // Check if file has a TOC block
  // Common TOC patterns:
  // ## MỤC LỤC / ## Mục lục / ## TABLE OF CONTENTS
  // followed by a list of - [Title](#anchor)
  // followed by --- or next heading
  const tocRegex = /(##\s+(?:MỤC LỤC|Mục lục|TABLE OF CONTENTS|Table of Contents)[^\n]*\n)([\s\S]*?)(\n---|\n##\s+)/i;
  const tocMatch = content.match(tocRegex);

  if (tocMatch) {
    console.log(`Found TOC in: ${relPath}`);
    
    // Extract all headings after the TOC section
    const lines = content.split('\n');
    const slugCounts = {};
    const headings = [];

    let insideToc = false;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      if (/^##\s+(?:MỤC LỤC|Mục lục|TABLE OF CONTENTS|Table of Contents)/i.test(line)) {
        insideToc = true;
        continue;
      }
      if (insideToc) {
        if (/^##\s+/.test(line)) {
          insideToc = false;
        } else {
          continue;
        }
      }

      const hMatch = line.match(/^(#{2,4})\s+(.+)$/);
      if (hMatch) {
        const level = hMatch[1].length; // 2, 3, 4
        const text = hMatch[2].trim();
        // Skip document control / info sections if desired or keep all
        if (/^(THÔNG TIN TÀI LIỆU|DOCUMENT CONTROL|LỊCH SỬ THAY ĐỔI|BẢNG THAY ĐỔI)/i.test(text)) {
          // keep or skip
        }
        let slug = toGfmSlug(text);
        if (slugCounts[slug] !== undefined) {
          slugCounts[slug]++;
          slug = `${slug}-${slugCounts[slug]}`;
        } else {
          slugCounts[slug] = 0;
        }
        headings.push({ level, text, slug });
      }
    }

    // Build new TOC lines
    const newTocLines = headings.map(h => {
      const indent = '  '.repeat(h.level - 2);
      return `${indent}- [${h.text}](#${h.slug})`;
    }).join('\n');

    const newTocBlock = `${tocMatch[1]}\n${newTocLines}\n${tocMatch[3]}`;
    content = content.replace(tocRegex, newTocBlock);
    fs.writeFileSync(file, content, 'utf8');
    console.log(`  -> Updated TOC for ${relPath}`);
  }
});
