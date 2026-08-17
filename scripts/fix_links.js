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
    console.log(`[FIXED] ${relPath}`);
  }
}

// 1. Fix 02-planning/03-product-backlog.md
fixFile('02-planning/03-product-backlog.md', [
  [/06-architecture\.md/g, '02-architecture.md'],
  [/docs\/06-architecture\.md/g, '02-architecture.md'],
  [/docs\/07-product-backlog\.md/g, '03-product-backlog.md']
]);

// 2. Fix 02-planning/04-cost-time-resource.md
fixFile('02-planning/04-cost-time-resource.md', [
  [/\.\/project_log\.md/g, '../03-execution-monitoring/02-project-log.md'],
  [/project_log\.md/g, '../03-execution-monitoring/02-project-log.md'],
  [/images\//g, '../assets/images/']
]);

// 3. Fix 02-planning/05-statement-of-work.md
fixFile('02-planning/05-statement-of-work.md', [
  [/project_log\.md/g, '../03-execution-monitoring/02-project-log.md']
]);

// 4. Fix 01-initiation/05-team-contract.md
fixFile('01-initiation/05-team-contract.md', [
  [/project_log\.md/g, '../03-execution-monitoring/02-project-log.md']
]);

// 5. Fix 03-execution-monitoring/03-ai-development-workflow.md
fixFile('03-execution-monitoring/03-ai-development-workflow.md', [
  [/07-product-backlog\.md/g, '../02-planning/03-product-backlog.md'],
  [/\.\/project_log\.md/g, './02-project-log.md'],
  [/images\/ai_workflow_pattern\.svg/g, '../assets/images/ai_workflow_pattern.svg'],
  [/images\/ai_token_distribution\.svg/g, '../assets/images/ai_token_distribution.svg'],
  [/images\/ai_hours_per_session\.svg/g, '../assets/images/ai_hours_per_session.svg'],
  [/images\/ai_token_efficiency\.svg/g, '../assets/images/ai_token_efficiency.svg']
]);

// 6. Fix 04-review-presentation/02-project-evaluation-qa.md
fixFile('04-review-presentation/02-project-evaluation-qa.md', [
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/01-project-idea\.md/g, '../01-initiation/01-project-idea.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/02-project-proposal\.md/g, '../01-initiation/02-project-proposal.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/04-feasibility-study\.md/g, '../01-initiation/03-feasibility-study.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/05-project-charter\.md/g, '../01-initiation/04-project-charter.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/11-team-contract\.md/g, '../01-initiation/05-team-contract.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/03-vision-and-scope\.md/g, '../02-planning/01-vision-and-scope.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/06-architecture\.md/g, '../02-planning/02-architecture.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/07-product-backlog\.md/g, '../02-planning/03-product-backlog.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/08-cost-time-resource\.md/g, '../02-planning/04-cost-time-resource.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/10-statement-of-work\.md/g, '../02-planning/05-statement-of-work.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/09-ai-development-workflow-report\.md/g, '../03-execution-monitoring/03-ai-development-workflow.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/plan\.md/g, '../03-execution-monitoring/01-sprint-plan.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/project_log\.md/g, '../03-execution-monitoring/02-project-log.md'],
  [/file:\/\/\/[a-zA-Z]:\/[^)]+\/docs\/project_log\.md/g, '../03-execution-monitoring/02-project-log.md']
]);

// 7. Fix 04-review-presentation/01-midterm-requirement.md
const midPath = path.join(docsDir, '04-review-presentation/01-midterm-requirement.md');
if (fs.existsSync(midPath)) {
  let content = fs.readFileSync(midPath, 'utf8');
  content = content.replace(/Thyết trình/g, 'Thuyết trình');
  if (!content.startsWith('#')) {
    content = `# HƯỚNG DẪN VÀ YÊU CẦU BÁO CÁO GIỮA KỲ (MIDTERM REQUIREMENTS)\n\n` + content;
  }
  fs.writeFileSync(midPath, content, 'utf8');
  console.log('[FIXED] 04-review-presentation/01-midterm-requirement.md');
}

// 8. Fix Slide references
fixFile('04-review-presentation/slide/pages/04-development-method.md', [
  [/project_log\.md/g, '../../03-execution-monitoring/02-project-log.md']
]);
fixFile('04-review-presentation/slide/pages/05-estimation-planning-monitoring.md', [
  [/project_log\.md/g, '../../03-execution-monitoring/02-project-log.md']
]);
