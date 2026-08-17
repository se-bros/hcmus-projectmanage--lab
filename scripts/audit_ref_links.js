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
const potentialBrokenRefLinks = [];

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8').replace(/\r\n/g, '\n');
  const lines = content.split('\n');

  lines.forEach((line, idx) => {
    // Ignore checkboxes like - [ ] or - [x] or * [ ]
    let sanitizedLine = line.replace(/^[ \t]*[-*+]\s+\[[ xX]\]/g, '');
    // Ignore markdown links [text](url)
    sanitizedLine = sanitizedLine.replace(/\[([^\]]+)\]\([^)]+\)/g, '');
    // Ignore images ![alt](url)
    sanitizedLine = sanitizedLine.replace(/!\[([^\]]*)\]\([^)]+\)/g, '');
    // Ignore code blocks or inline code `...`
    sanitizedLine = sanitizedLine.replace(/`[^`]+`/g, '');
    // Ignore footnote definitions [^1]: ... or [ref]: ...
    if (/^[ \t]*\[\^?[^\]]+\]:\s+/.test(line)) return;

    // Now find any remaining standalone [text]
    const refMatch = sanitizedLine.match(/\[([^\]\n]+)\]/g);
    if (refMatch) {
      refMatch.forEach(m => {
        // Skip [^1] if footnote
        if (/^\[\^[\w\d]+\]$/.test(m)) return;
        // Check if there's a matching definition in the file
        const label = m.slice(1, -1).trim();
        const defRegex = new RegExp(`^[ \\t]*\\[${label.replace(/[.*+?^${}()|[\\]\\]/g, '\\$&')}\\]:\\s+`, 'm');
        if (!defRegex.test(content)) {
          potentialBrokenRefLinks.push({
            file: relPath,
            lineNum: idx + 1,
            rawText: m,
            label,
            lineContent: line.trim()
          });
        }
      });
    }
  });
});

console.log('--- POTENTIAL UNRESOLVED REFERENCE LINKS ---');
console.log(JSON.stringify(potentialBrokenRefLinks, null, 2));
