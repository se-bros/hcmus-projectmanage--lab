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
const brokenAssets = [];

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');

  // Match markdown images: ![alt](path)
  const imgRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;
  let match;
  while ((match = imgRegex.exec(content)) !== null) {
    const rawSrc = match[2].split('#')[0].split('?')[0];
    if (rawSrc.startsWith('http://') || rawSrc.startsWith('https://')) continue;

    let resolved;
    if (rawSrc.startsWith('/')) {
      resolved = path.join(docsDir, rawSrc);
    } else {
      resolved = path.resolve(path.dirname(file), rawSrc);
    }
    if (!fs.existsSync(resolved)) {
      brokenAssets.push({
        file: relPath,
        type: 'image',
        raw: match[0],
        src: rawSrc,
        resolved
      });
    }
  }

  // Match html img tags: <img ... src="..." ... />
  const htmlImgRegex = /<img[^>]+src=["']([^"']+)["']/g;
  while ((match = htmlImgRegex.exec(content)) !== null) {
    const rawSrc = match[1].split('#')[0].split('?')[0];
    if (rawSrc.startsWith('http://') || rawSrc.startsWith('https://')) continue;

    let resolved;
    if (rawSrc.startsWith('/')) {
      resolved = path.join(docsDir, rawSrc);
    } else {
      resolved = path.resolve(path.dirname(file), rawSrc);
    }
    if (!fs.existsSync(resolved)) {
      brokenAssets.push({
        file: relPath,
        type: 'html-img',
        raw: match[0],
        src: rawSrc,
        resolved
      });
    }
  }
});

console.log('Broken Images/Assets Count:', brokenAssets.length);
console.log(JSON.stringify(brokenAssets, null, 2));
