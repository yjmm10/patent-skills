# Changelog

本文件记录 `paper-polish-skill` 每次改动的版本号与摘要。  
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)：`MAJOR.MINOR.PATCH`

- **MAJOR**：不兼容的流程/模式删除或重命名
- **MINOR**：新增模式、reference、prompt 或显著能力扩展
- **PATCH**：文案修正、检查清单微调、typo、无行为变化的澄清

---

## [1.4.1] — 2026-07-04

### Added
- 与 `project-uav-skill` v1.0.0 分工说明及 paper_bridge 协作链

---

## [1.4.0] — 2026-07-04

### Added
- `CHANGELOG.md`：集中记录各版本变更
- `SKILL.md` §版本管理：规定每次改动须 bump 版本并写 changelog

### Changed
- 维护流程：后续所有 skill 修改必须同步更新 frontmatter `version` 与本文件

---

## [1.3.0] — 2026-07-04

### Added
- `references/code-abstraction.md`：五层代码/实现细节抽象化策略
- `prompts/code_abstraction_polish.md`：`code_abstraction` 工作模式
- `final-checklist.md`：代码与实现抽象化检查项；诊断报告 P1d
- `evals/evals.json`：eval 6（去代码化）

### Changed
- `full_polish.md` / `diagnose.md` / `chapter-guidelines.md`：Method/Evaluation 自动应用代码抽象
- `figure-and-experiment.md`：Setup 节技术栈表述规范
- `sentence-templates.md`：实现/评估/奖励抽象化句式

---

## [1.2.0] — 2026-07-04

### Added
- `references/section-transitions.md`：战略/战术/操作三级章节过渡
- `prompts/transitions_polish.md`：`transitions` 工作模式
- `final-checklist.md`：子节过渡检查项；诊断报告 P1c
- `evals/evals.json`：eval 5（II→II-A 过渡）

### Changed
- `full_polish.md` / `diagnose.md` / `chapter-guidelines.md`：集成过渡润色流程
- `sentence-templates.md`：战略/战术/操作过渡速查句

---

## [1.1.0] — 2026-07-04

### Added
- `references/experiment-section-structure.md`：实验章 3/4/5 小节标准划分
- 实验章决策指南、六维↔小节映射、V-A–V-D 内容规范

### Changed
- `figure-and-experiment.md`：图表与小节对应关系
- `diagnose.md` / `section_polish.md` / `final-checklist.md`：实验小节结构诊断与润色
- `evals/evals.json`：更新 eval 2/3，新增 eval 4

---

## [1.0.0] — 2026-07-04

### Added
- 初始发布：`SKILL.md` 主流程与 5 种模式（full / section / diagnose / front / experiment）
- `references/`：chapter-guidelines、figure-and-experiment、writing-principles、sentence-templates、final-checklist
- `prompts/`：intake、diagnose、full_polish、section_polish、self_check、iteration
- `evals/evals.json`：eval 1–3
