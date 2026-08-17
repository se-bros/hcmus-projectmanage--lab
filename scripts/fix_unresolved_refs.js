const fs = require('fs');
const path = require('path');

const docsDir = path.resolve(__dirname, '../docs');

function fixFile(relPath, transforms) {
  const fullPath = path.join(docsDir, relPath);
  if (!fs.existsSync(fullPath)) return;
  let content = fs.readFileSync(fullPath, 'utf8');
  let original = content;
  transforms.forEach(([search, replace]) => {
    content = content.replace(search, replace);
  });
  if (content !== original) {
    fs.writeFileSync(fullPath, content, 'utf8');
    console.log(`[FIXED UNRESOLVED REFS] ${relPath}`);
  }
}

// 1. Fix 01-initiation/04-project-charter.md
fixFile('01-initiation/04-project-charter.md', [
  [/\[Đường găng - Critical Path\]/g, '(Đường găng - Critical Path)']
]);

// 2. Fix 04-review-presentation/02-project-evaluation-qa.md
fixFile('04-review-presentation/02-project-evaluation-qa.md', [
  [/`\[CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG\]`/g, '*(Chưa có trong 8 tài liệu gốc — để trống để bổ sung)*'],
  [/\[CHƯA CÓ TRONG 8 TÀI LIỆU GỐC - ĐỂ TRỐNG ĐỂ BỔ SUNG\]/g, '*(Chưa có trong 8 tài liệu gốc — để trống để bổ sung)*'],
  [/\[THAO TÁC DEMO TRỰC TIẾP ĐỂ TRỐNG ĐỂ BỔ SUNG\]/g, '*(Thao tác demo trực tiếp — để trống để bổ sung)*']
]);

// 3. Fix 04-review-presentation/slide/pages/05-estimation-planning-monitoring.md
fixFile('04-review-presentation/slide/pages/05-estimation-planning-monitoring.md', [
  [/\[ĐIỂM NGHẼN\]/g, '(ĐIỂM NGHẼN)']
]);
