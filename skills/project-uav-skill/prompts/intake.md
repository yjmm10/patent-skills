# Intake

## 判定模式

| 用户意图 | 模式 |
|----------|------|
| 设计新批次 / 几臂对照 | `batch_design` |
| 检查 run 能否复现、缺什么文件 | `archive_audit` |
| 不重训只重跑 eval | `reeval` |
| metrics → fig → section5 / 交 paper-polish | `paper_bridge` |
| 开大实验前先小规模试 | `smoke` |

## 必收集

- 项目路径（默认 `./uav-example` 或用户指定）
- 批次根：`runs_v1.x`
- arm 名（可多个）
- run_id（可选；默认 LATEST）

## 输出确认

```markdown
## 任务确认
- 模式：archive_audit
- 批次：runs_v1.2
- Arm：qmix_satcpp_uar
- Run：LATEST → run_20260702_060910
```

然后 Read 对应 prompt + reference。
