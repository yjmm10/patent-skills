# Batch Design

**Read** `experiment-protocol.md`、`project-layout.md`。

## 步骤

1. 明确论文表/消融要回答的问题
2. 列出 arm 表（每臂仅变创新维度）
3. 定批次 ID：`runs_v1.x` + `logs/v1.x`
4. 写 CHANGELOG 条目草案 + 脚本头注释
5. 确认 eval_suite 共享、config 基线路径

## 交付

- Arm 对照表
- CHANGELOG `[x.y.z]` 草案（含三问：测什么/差异/产出）
- `scripts/run_v1.x.sh` 修改要点（ARMS 列表、EP、resume 策略）
