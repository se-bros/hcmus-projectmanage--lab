const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

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

console.log('--- AUDITING DOCUMENT METADATA ---');
mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');
  
  // Extract Title and Document ID if exists
  const titleMatch = content.match(/^#\s+(.+)$/m);
  const docIdMatch = content.match(/Mã tài liệu.*?`([^`]+)`/i) || content.match(/Document ID.*?`([^`]+)`/i);
  
  console.log(`[${relPath}]`);
  console.log(`  Title: ${titleMatch ? titleMatch[1] : 'N/A'}`);
  console.log(`  Doc ID: ${docIdMatch ? docIdMatch[1] : 'N/A'}`);
});
