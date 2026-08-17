const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

function getAllFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      if (file !== 'node_modules' && file !== '.git') getAllFiles(fullPath, fileList);
    } else if (file.endsWith('.md')) {
      fileList.push(fullPath);
    }
  });
  return fileList;
}

const mdFiles = getAllFiles(docsDir);

console.log('--- HEADINGS WITH SLASH OR SPECIAL CHARACTERS ---');
mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    if (/^#{1,6}\s+/.test(line)) {
      if (line.includes('/') || line.includes('&') || line.includes('--') || line.includes(':')) {
        console.log(`${relPath}:${idx+1} -> ${line.trim()}`);
      }
    }
  });
});
