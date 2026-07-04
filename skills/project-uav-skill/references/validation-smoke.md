# 开大实验前 Smoke 预检

完整 `validate.py` 流水线为可选扩展；v1 用 **清单 + 短 run** 降低浪费。

## Smoke 配置建议

| 项 | Smoke | 正式 |
|----|-------|------|
| max_episodes | 50–100 | 2000–40000 |
| eval_every | 25–50 | 1000 |
| arms | 1 代表臂 | 全批 |

## 预检清单（开跑前）

- [ ] `VERSION` / `CHANGELOG` 已更新批次说明
- [ ] `config/default.yaml` 与 arm 表一致
- [ ] eval_suite manifest 将写入批次根
- [ ] `RunManager` LATEST 逻辑确认（resume vs fresh）
- [ ] 磁盘空间（checkpoint × arms）

## 短 run 后自动检查

| 检查 | 条件 | 动作 |
|------|------|------|
| 奖励停滞 | 最近 10 ep std < 1e-6 | 查 reward/obs 常数 |
| 奖励暴跌 | 近 10 ep 均值 < 历史 50% | 查 lr/clip/环境 |
| Loss 异常 | NaN / Inf | 停批，修网络或梯度 |
| 指标越界 | HUOT/DMR 等超出物理可能 | 查公式与 log 字段 |
| 无 eval 写入 | smoke 结束无 metrics 行 | 查 eval_every / 路径 |

## 理论边界（可选，领域相关）

uav-example 用 HUOT/DMR/deadline 等；**边界须来自论文 §3–4**，非硬编码 universal 阈值。Smoke 只验证「非平凡变化 + 无 NaN」，不用 mock 理论 0.95–1.0 表。

## 通过后

- CHANGELOG 记「smoke pass @ ep=100」
- 启动正式 `run_v1.x.sh`
- `monitor_arms.sh` 盯盘

## 排除（v1 不做）

- 自动化 mock 同行评审
- 全量 CI 门禁（可后续 `.github/workflows` reference）
