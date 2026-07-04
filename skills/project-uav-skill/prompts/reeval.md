# Re-eval（不重训）

**Read** `data-archival-contract.md`、`experiment-protocol.md`。

## 前提

- 等级 ≥ B：有 checkpoint + eval_suite + config
- 明确 checkpoint：`best_reward.pt` / `latest.pt` / `ep{N}.pt`

## 步骤

1. 确认 eval_suite manifest 与训练时一致
2. 指向 uav-example 入口（或项目等价物）：
   - `evaluate_final.py` / `run_experiment --eval-only` 等
3. 输出写入 run 目录或 `run_logs/eval_rerun_<ts>.jsonl`
4. **不**删除原 metrics；新 eval 单独文件或标注 ep/source

## 禁止

- 无 eval_suite 仍声称与主表可比
- 覆盖原 metrics.jsonl 无备份
