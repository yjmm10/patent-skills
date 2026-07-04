---
name: project-uav-skill
description: >-
  Use when building, running, or auditing UAV multi-agent RL research repos (QMIX/MAPPO, SATCPP/UAR): experiment batches (runs_v1.x), RunManager/LATEST resume, checkpoint and metrics archival, fixed eval_suite re-eval without re-training, fig scripts to paper Section V. Also use for archive audits, arm batch design, or bridging runs to paper-polish-skill. Not for generic PPO scaffolding or writing papers from scratch.
version: "1.0.0"
user-invocable: true
argument-hint: "[可选：批次名/ arm / runs 路径 / archive|reeval|paper_bridge]"
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, Bash
---

# Project UAV — 科研代码库与实验协议

面向 **UAV + 多智能体 RL** 论文复现型项目（参考 `uav-example` 已验证实践）。管理 **实验批次 → 数据存档 → 重评估 → 论文 Fig/Section V**，与 **`paper-polish-skill`** 分工：本 skill 管代码与 runs；润色管表达。

分步指令在 **`prompts/`**，规范在 **`references/`**——执行前 **`Read`** 对应文件。

---

## 与 `paper-polish-skill` 的分工

| 场景 | 使用技能 |
|------|----------|
| 目录结构、跑实验、续训、存档、eval_suite 重评估 | **本 skill** |
| Section V 结构、过渡、代码抽象化、全文润色 | `paper-polish-skill` |
| runs → fig 数据 → section5 草稿 | 本 skill **`paper_bridge`** → 再交 paper-polish |

---

## 触发条件

- 实验批次、`runs_v1.x`、arm、LATEST、续训 `--resume`
- checkpoint / metrics.jsonl / eval_suite 存档或缺失
- 不重训只重评估、evaluate_final、fig 脚本
- 斜杠：`/project-uav`、`/uav-lab`

**不触发**：从零写论文全文 → `paper-polish-skill`；与 UAV 无关的通用 RL 模板。

---

## 工作模式

| 模式 | 场景 | Prompt + Reference |
|------|------|-------------------|
| `batch_design` | 新批次、多臂对照设计 | `batch_design.md` + `experiment-protocol.md` |
| `archive_audit` | 检查 run 是否可复现/可重评估 | `archive_audit.md` + `data-archival-contract.md` |
| `reeval` | 用 checkpoint + eval_suite 重跑 eval | `reeval.md` + `data-archival-contract.md` |
| `paper_bridge` | runs → fig → section5 | `paper_bridge.md` + `paper-bridge.md` |
| `smoke` | 小批量预检再开大实验 | `smoke.md` + `validation-smoke.md` |

未说明时：有 runs 路径 → `archive_audit`；要设计实验 → `batch_design`。

---

## 主流程概览

```
intake → 选模式 → Read references → 执行 prompts → 交付（含版本/批次说明）
```

**intake**：`prompts/intake.md`

---

## 交付格式

1. **结论摘要**（批次/arm/路径/存档状态）
2. **检查表** ✅/⚠️/❌（archive_audit / smoke）
3. **CHANGELOG 建议条目**（新批次时）
4. **paper_bridge**：fig 输入路径 + section5 片段或交 paper-polish 的说明

保存建议：`./outputs/{批次}/{arm}/audit_{timestamp}.md`

---

## Reference 索引

| 文件 | 何时 Read |
|------|-----------|
| `references/project-layout.md` | 搭项目、找模块、对照 uav-example |
| `references/experiment-protocol.md` | 批次、arm、LATEST、续训 |
| `references/data-archival-contract.md` | 存档审计、重评估 |
| `references/validation-smoke.md` | 开大实验前预检 |
| `references/paper-bridge.md` | runs → 论文 Section V / fig |

---

## 版本管理

**当前版本**：frontmatter + **`CHANGELOG.md`**。修改本 skill 须 bump 版本并写 changelog。

---

## Prompt 映射

| 文件 | 用途 |
|------|------|
| `prompts/intake.md` | 模式判定 |
| `prompts/batch_design.md` | 实验批次与 arm 表 |
| `prompts/archive_audit.md` | 存档合规审计 |
| `prompts/reeval.md` | 不重训重评估 |
| `prompts/paper_bridge.md` | 对接 paper-polish |
| `prompts/smoke.md` | 小批量 smoke |
