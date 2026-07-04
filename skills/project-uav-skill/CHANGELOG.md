# Changelog

版本遵循语义化版本 `MAJOR.MINOR.PATCH`。

---

## [1.0.0] — 2026-07-04

### Added
- 初始发布：UAV 科研代码库与实验协议 skill（由 uav-example 实践沉淀）
- `references/`：project-layout、experiment-protocol、data-archival-contract、validation-smoke、paper-bridge
- `prompts/`：intake、batch_design、archive_audit、reeval、paper_bridge、smoke
- `evals/evals.json`：3 条测试 prompt
- 与 `paper-polish-skill` v1.4.1 cross-ref

### 设计来源
- 已验证：`uav-example` RunManager、CheckpointManager、eval_suite、runs_v1.x 批次、VERSION/CHANGELOG
- 纳入：实验目的可追溯、数据永久存档、允许重评估不重训
- 排除 v1：mock 同行评审、泛化 PPO/SAC 目录树
