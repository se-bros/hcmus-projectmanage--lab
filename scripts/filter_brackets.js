const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

function getAllFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (file !== 'node_modules' && file !== '.git' && file !== 'slide') getAllFiles(fullPath, fileList);
    } else if (file.endsWith('.md')) {
      fileList.push(fullPath);
    }
  });
  return fileList;
}

const mdFiles = getAllFiles(docsDir);
const results = [];

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  const lines = content.split('\n');

  lines.forEach((line, idx) => {
    // skip checkboxes
    let l = line.replace(/^[ \t]*[-*+]\s+\[[ xX]\]/g, '');
    // skip full links [text](url)
    l = l.replace(/\[([^\]]+)\]\([^)]+\)/g, '');
    // skip images
    l = l.replace(/!\[([^\]]*)\]\([^)]+\)/g, '');
    // skip inline code
    l = l.replace(/`[^`]+`/g, '');
    // skip html tags
    l = l.replace(/<[^>]+>/g, '');

    const matches = l.match(/\[([^\]]+)\]/g);
    if (matches) {
      matches.forEach(m => {
        results.push({
          file: relPath,
          lineNum: idx + 1,
          match: m,
          lineText: line.trim()
        });
      });
    }
  });
});

console.log('--- STANDALONE BRACKETS IN DOCS (EXCLUDING SLIDES) ---');
console.log(JSON.stringify(results, null, 2));
