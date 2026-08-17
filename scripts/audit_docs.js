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
console.log('Total Markdown files in docs:', mdFiles.length);

const brokenLinks = [];
const referencesFound = [];

mdFiles.forEach(file => {
  const relPath = path.relative(docsDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');

  // Check markdown links
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
  let match;
  while ((match = linkRegex.exec(content)) !== null) {
    const rawLink = match[2];
    const linkTarget = rawLink.split('#')[0].split('?')[0];
    if (linkTarget.startsWith('http://') || linkTarget.startsWith('https://') || linkTarget.startsWith('mailto:') || linkTarget.startsWith('#') || linkTarget === '') {
      continue;
    }
    let resolved;
    if (linkTarget.startsWith('file:///')) {
      resolved = linkTarget.replace('file:///', '').replace(/^[a-zA-Z]:/, m => m.toLowerCase());
    } else {
      resolved = path.resolve(path.dirname(file), linkTarget);
    }
    if (!fs.existsSync(resolved)) {
      brokenLinks.push({
        file: relPath,
        link: rawLink,
        resolved
      });
    }
  }

  // Check mentions of old doc names in text
  const textCheck = [
    '01-project-idea.md',
    '02-project-proposal.md',
    '03-vision-and-scope.md',
    '04-feasibility-study.md',
    '05-project-charter.md',
    '06-architecture.md',
    '07-product-backlog.md',
    '08-cost-time-resource.md',
    '09-ai-development-workflow-report.md',
    '10-statement-of-work.md',
    '11-team-contract.md',
    'plan.md',
    'project_log.md',
    'note_summary.md',
    'midterm_requirement.md',
    'project-evaluation-qa.md'
  ];

  textCheck.forEach(item => {
    if (content.includes(item)) {
      referencesFound.push({
        file: relPath,
        mention: item
      });
    }
  });
});

console.log('\n--- BROKEN LINKS FOUND ---');
console.log(JSON.stringify(brokenLinks, null, 2));

console.log('\n--- OLD FILENAME MENTIONS ---');
console.log(JSON.stringify(referencesFound, null, 2));
