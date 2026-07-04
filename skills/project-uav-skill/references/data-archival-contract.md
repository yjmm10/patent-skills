# 数据存档契约

**原则**：论文定稿后应能 **不重训、可重评估、可重画图**。训练昂贵；eval 与 fig 可重复。

## 必存档清单（每个 active run）

| 路径 | 必需 | 用途 |
|------|------|------|
| `config.yaml` | ✅ | 完整复现 hyperparam + arm |
| `checkpoints/latest.pt` | ✅ | 续训 / 中断恢复 |
| `checkpoints/best_reward.pt` | ✅ | 报告最优模型 |
| `checkpoints/ep{N}.pt` | 推荐 | 周期性快照 |
| `run_state.json` | 推荐 | 无 torch 读 episode/best |
| `metrics.jsonl` | ✅ | eval 曲线、论文 Fig 收敛 |
| `train_log.jsonl` | ✅ | 训练过程诊断 |
| `run_logs/eval_*.jsonl` | ✅ | 单次 run 切片，resume 不丢历史 |

## 批次级必存档

| 路径 | 必需 | 用途 |
|------|------|------|
| `eval_suite_n*.json` | ✅ | 固定 hold-out 200 场景；**重评估唯一依据** |
| 共享 env layout（如有） | 推荐 | 轨迹图一致 |

## 允许的操作（无需重训）

1. **`evaluate_final`** / 加载 `best_reward.pt` 或 `latest.pt` + eval_suite
2. **`scripts/fig_*.py`** 读 `metrics.jsonl` / eval jsonl 重出图
3. **paper_bridge** 更新 section5 文字（数据不变）

## 禁止

- 仅保留 png/pdf 而删除 metrics/checkpoint
- 论文引用数字但 run 目录无对应 ep 记录
- 改 eval_suite 后不重标注批次 ID

## 审计等级

| 等级 | 条件 |
|------|------|
| **A 可发表** | 必存档全开 + 批次 eval_suite + VERSION/CHANGELOG 对齐 |
| **B 可重评估** | checkpoint + eval_suite + config；metrics 完整 |
| **C 仅可续训** | latest.pt + config；缺 eval_suite 或 metrics |
| **F 不可复现** | 无 config 或无 checkpoint |

## 审计输出模板

```markdown
## 存档审计 — {arm} / {run_id}

| 项 | 状态 | 路径 |
|----|------|------|
| config.yaml | ✅ | ... |
| eval_suite (batch) | ⚠️ 缺失 | 需 regenerate |

**等级**：B  
**建议**：运行 save_eval_suite_manifest + evaluate_final
```
