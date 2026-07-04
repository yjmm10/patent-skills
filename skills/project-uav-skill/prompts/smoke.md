# Smoke

**Read** `validation-smoke.md`。

## 步骤

1. 跑预检清单（未开批前）
2. 建议 smoke 命令（1 arm，50–100 ep）
3. 读 smoke run 的 metrics/train_log 做异常检查
4. 通过 → 给出正式批启动命令；失败 → 根因 + 停批

## 交付

- 预检 ✅/❌
- smoke 结果摘要
- 是否批准启动 `run_v1.x.sh`
