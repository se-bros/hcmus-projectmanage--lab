import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(BASE_DIR, 'docs.1', 'evidence')

def copy_file(src, dst_dir, custom_name=None):
    if not os.path.exists(src):
        print(f"Warning: Source not found: {src}")
        return False
    os.makedirs(dst_dir, exist_ok=True)
    filename = custom_name if custom_name else os.path.basename(src)
    dst = os.path.join(dst_dir, filename)
    shutil.copy2(src, dst)
    print(f"Copied: {src} -> {dst}")
    return True

def copy_tree_files(src_dir, dst_dir, prefix=""):
    if not os.path.exists(src_dir):
        print(f"Warning: Source dir not found: {src_dir}")
        return
    os.makedirs(dst_dir, exist_ok=True)
    for root, _, files in os.walk(src_dir):
        for f in files:
            src_file = os.path.join(root, f)
            rel = os.path.relpath(src_file, src_dir)
            target_name = f"{prefix}_{rel.replace(os.sep, '_')}" if prefix else rel.replace(os.sep, '_')
            dst_file = os.path.join(dst_dir, target_name)
            shutil.copy2(src_file, dst_file)
            print(f"Copied: {src_file} -> {dst_file}")

def main():
    # 01 - Proposal
    q01 = os.path.join(EVIDENCE_DIR, '01')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '01-project-proposal.pdf'), q01)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '1_Initiation_Charter_Feasibility', 'assets', 'q1_proposal_flow.svg'), q01)

    # 02 - Vision & Scope
    q02 = os.path.join(EVIDENCE_DIR, '02')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '02-vision-and-scope.pdf'), q02)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '2_Requirements_Scope_SoW', 'diagrams', 'vision-as-is-to-be.svg'), q02)

    # 03 - Charter
    q03 = os.path.join(EVIDENCE_DIR, '03')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '03-project-charter.pdf'), q03)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '1_Initiation_Charter_Feasibility', 'assets', 'q3_charter_governance.svg'), q03)

    # 04 - Requirements & Backlog & User Guide
    q04 = os.path.join(EVIDENCE_DIR, '04')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '04-software-requirements.pdf'), q04)
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '04-product-backlog.pdf'), q04)
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '04-user-guide.pdf'), q04)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '2_Requirements_Scope_SoW', 'diagrams', 'requirements-traceability.svg'), q04)

    # 05 - Architecture & ADR
    q05 = os.path.join(EVIDENCE_DIR, '05')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '05-software-architecture.pdf'), q05)
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', 'A1-decision-log-and-adr.pdf'), q05)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q5', 'context_diagram.svg'), q05)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q5', 'system_architecture.svg'), q05)

    # 06 - PoC
    q06 = os.path.join(EVIDENCE_DIR, '06')
    copy_tree_files(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q6', 'poc-1'), q06, prefix="poc1")
    copy_tree_files(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q6', 'poc-2'), q06, prefix="poc2")
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q6', 'test-passed.png'), q06)

    # 07 - Prototype
    q07 = os.path.join(EVIDENCE_DIR, '07')
    copy_tree_files(os.path.join(BASE_DIR, 'final-exam', 'preparation', '3_Architecture_PoC_Prototype', 'printouts', 'Q7'), q07)
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'md', 'assets', 'prototype-core-flow.svg'), q07)

    # 08 - Feasibility
    q08 = os.path.join(EVIDENCE_DIR, '08')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '08-feasibility-study.pdf'), q08)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '1_Initiation_Charter_Feasibility', 'assets', 'q8_telos_assessment.svg'), q08)

    # 09 - Process
    q09 = os.path.join(EVIDENCE_DIR, '09')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '09-software-process-definition.pdf'), q09)

    # 10 - Estimate
    q10 = os.path.join(EVIDENCE_DIR, '10')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '10-project-estimate.pdf'), q10)
    copy_file(os.path.join(BASE_DIR, 'docs', 'assets', 'images', 'capex_breakdown.svg'), q10)

    # 11 - Project Plan
    q11 = os.path.join(EVIDENCE_DIR, '11')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '11-project-plan.pdf'), q11)
    copy_file(os.path.join(BASE_DIR, 'docs', 'assets', 'images', 'project_roadmap.svg'), q11)
    copy_file(os.path.join(BASE_DIR, 'docs', 'assets', 'images', 'project_timeline.svg'), q11)

    # 12 - SOW
    q12 = os.path.join(EVIDENCE_DIR, '12')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '12-statement-of-work.pdf'), q12)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '2_Requirements_Scope_SoW', 'diagrams', 'sow-change-control.svg'), q12)

    # 13 - CI
    q13 = os.path.join(EVIDENCE_DIR, '13')
    copy_file(os.path.join(BASE_DIR, '.github', 'workflows', 'ci.yml'), q13)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '5_CICD_DevOps_Testing', 'printouts', 'Q13', 'CI-pass.png'), q13)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '5_CICD_DevOps_Testing', 'printouts', 'Q13', 'Mail.png'), q13)
    copy_file(os.path.join(BASE_DIR, 'docs', '03-execution-monitoring', '06-developer-guide.md'), q13)

    # 14 - CD
    q14 = os.path.join(EVIDENCE_DIR, '14')
    copy_file(os.path.join(BASE_DIR, '.github', 'workflows', 'cd.yml'), q14)
    copy_file(os.path.join(BASE_DIR, 'docker-compose.prod.yml'), q14)
    copy_tree_files(os.path.join(BASE_DIR, 'final-exam', 'preparation', '5_CICD_DevOps_Testing', 'printouts', 'Q14'), q14)
    copy_file(os.path.join(BASE_DIR, 'docs', '03-execution-monitoring', '07-deployment-guide.md'), q14)

    # 15 - DevOps & Terraform
    q15 = os.path.join(EVIDENCE_DIR, '15')
    copy_tree_files(os.path.join(BASE_DIR, 'final-exam', 'preparation', '5_CICD_DevOps_Testing', 'printouts', 'Q15'), q15)
    if os.path.exists(os.path.join(BASE_DIR, 'terraform')):
        copy_tree_files(os.path.join(BASE_DIR, 'terraform'), q15, prefix="terraform")

    # 16 - Team Contract & Members
    q16 = os.path.join(EVIDENCE_DIR, '16')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '16-team-contract.pdf'), q16)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', 'images', 'group3-photo.png'), q16)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', 'images', 'discord_communication.png'), q16)

    # 17 - Monitoring & Tracking
    q17 = os.path.join(EVIDENCE_DIR, '17')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '17-project-log.pdf'), q17)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', 'images', 'trello_kanban_board.png'), q17)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', 'images', 'burndown_chart.png'), q17)

    # 18 - Risk Plan
    q18 = os.path.join(EVIDENCE_DIR, '18')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '18-risk-management-plan.pdf'), q18)

    # 19 - Quality Plan
    q19 = os.path.join(EVIDENCE_DIR, '19')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '19-quality-management-plan.pdf'), q19)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', '01_code_inspection_record_pr41.md'), q19)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', '02_uat_feedback_record.md'), q19)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', '03_coding_standards_and_linter_config.md'), q19)

    # 20 - Test Plan & Summary
    q20 = os.path.join(EVIDENCE_DIR, '20')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '20-test-plan.pdf'), q20)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '5_CICD_DevOps_Testing', 'printouts', 'Q20', 'run-test.png'), q20)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', '01_code_inspection_record_pr41.md'), q20)
    copy_file(os.path.join(BASE_DIR, 'final-exam', 'preparation', '6_Team_Monitoring_Risk_Lessons', '02_uat_feedback_record.md'), q20)

    # 21 - Lessons Learned
    q21 = os.path.join(EVIDENCE_DIR, '21')
    copy_file(os.path.join(BASE_DIR, 'docs.1', 'pdf', '21-lessons-learned.pdf'), q21)

    print("\nAll evidence artifacts populated successfully!")

if __name__ == '__main__':
    main()
