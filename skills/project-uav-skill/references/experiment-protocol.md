# 实验协议：批次、Arm、Run、续训

## 三层命名

| 层 | 示例 | 含义 |
|----|------|------|
| **代码版本** | `VERSION` 1.2.1 | 仓库逻辑变更 |
| **实验批次** | `runs_v1.2` | 一次论文表/消融对应的整批 run |
| **Arm** | `qmix_satcpp_uar` | 单变量对照臂 |
| **Run** | `run_20260702_060910` | 某 arm 的一次训练实例 |

## 实验批次必答三问

写入 `CHANGELOG.md` 该版本条目 + 批次脚本头注释：

1. **测什么**：对照哪些模块（如 rule vs satcpp vs +UAR vs Transformer）
2. **与上一批差异**：代码/奖罚/eval 协议变更
3. **产出物**：目标 ep、主表指标（HUOT、DMR 等）

## Arm 设计表模板

```markdown
| Arm | 感知/模块 A | 模块 B | 骨干 | 训练 | Eval 模式 |
|-----|-------------|--------|------|------|-----------|
| qmix_rule | rule 76.2% | — | GRU | QMIX | qmix greedy |
| qmix_satcpp_uar | satcpp | UAR ✓ | GRU | QMIX | qmix greedy |
```

规则：**每臂只变一行创新维度**；其余 hyperparam、env、eval_seed 锁定。

## RunManager 行为（与 uav-example 一致）

```
runs_v1.2/<arm>/
├── LATEST                 → 文本内容为 run_20260702_060910
└── run_20260702_060910/
    ├── checkpoints/
    ├── config.yaml
    ├── metrics.jsonl
    └── run_logs/
```

| 操作 | 行为 |
|------|------|
| `--no-resume` | 新建 `run_<ts>`，更新 LATEST，**不覆盖**旧 run |
| `--resume` | 读 LATEST → 继续该 run 的 checkpoint |
| 同秒冲突 | `run_<ts>_2` 后缀 |

## 批次脚本约定

- `scripts/run_v1.2.sh`：启动前写 **eval_suite manifest**（全 arm 共享）
- 环境布局一次渲染到批次根（公平对比）
- `logs/v1.2/arm_<name>.log` 保留 stdout
- 环境变量：`ARMS=` 子集重跑、`NO_RESUME=1` 强制新 run

## 续训至更高 ep

- CHANGELOG 记录：如 1.2.2「30000 → 40000 ep `--resume`」
- **同一 run 目录**内续训；metrics 追加，dedup 防重复 ep

## 禁止

- 在同一 run 上改 config 语义却不新 run（污染对照）
- 仅改输出路径覆盖旧 metrics
- 批次间混用不同 `eval_suite` seed 而无说明
