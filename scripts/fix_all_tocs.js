const fs = require('fs');
const path = require('path');

function generateSlug(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s\u00C0-\u1EF9-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

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

const allMdFiles = [
  ...getAllFiles(path.resolve('docs')),
  ...getAllFiles(path.resolve('final-exam'))
];

allMdFiles.forEach(file => {
  let content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  
  if (/^##\s+Mục lục/m.test(content)) {
    const lines = content.split('\n');
    let pastToc = false;
    const headings = [];

    lines.forEach(line => {
      if (/^##\s+Mục lục/.test(line)) {
        pastToc = true;
        return;
      }
      if (!pastToc) return;

      const h2 = line.match(/^##\s+(?!Mục lục)(.+)$/);
      const h3 = line.match(/^###\s+(.+)$/);

      if (h2) {
        const title = h2[1].trim();
        const slug = generateSlug(title);
        headings.push(`- [${title}](#${slug})`);
      } else if (h3) {
        const title = h3[1].trim();
        const slug = generateSlug(title);
        headings.push(`  - [${title}](#${slug})`);
      }
    });

    const newTocBlock = `## Mục lục\n\n${headings.join('\n')}\n\n---`;
    content = content.replace(/^##\s+Mục lục\s*\n[\s\S]*?(?=\n##\s+[0-9A-ZÀ-Ỹ]|\n---\n##\s+[0-9A-ZÀ-Ỹ])/m, newTocBlock);
    fs.writeFileSync(file, content, 'utf8');
    console.log('Fixed TOC & separator for:', path.relative(process.cwd(), file));
  }
});
