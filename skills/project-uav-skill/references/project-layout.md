# 项目目录与模块边界

> 对齐 `uav-example` 已验证布局；**不**采用泛化 `envs/ppo/sac/` 树，避免与论文 arm 语义脱节。

## 标准目录

```
project_root/
├── src/
│   ├── core/           # 环境、奖励、领域模块（grid_env, satcpp, uar, workload…）
│   ├── algo/           # qmix, mappo, base, networks
│   ├── training/       # config, trainer, run_manager, checkpoint, eval_suite
│   ├── experiments/    # run_experiment, run_all, evaluate_*, stats
│   └── figure/         # 论文级绘图（heatmap, traj, plots）
├── config/
│   └── default.yaml    # ExperimentConfig 基线
├── scripts/
│   ├── run_v1.x.sh     # 批次启动（多 arm 并行）
│   ├── monitor_arms.sh
│   └── fig_*.py        # 从 metrics 出图
├── runs_v1.x/          # 实验批次根（非 experiments/ppo/）
│   └── <arm>/
│       ├── LATEST      # 当前 active run_id（文本文件）
│       └── run_<ts>/
├── logs/v1.x/          # 各 arm 训练 stdout
├── paper/              # section 草稿
├── results/            # 汇总表、对比 md
├── VERSION             # 代码版本（与 CHANGELOG 同步）
├── CHANGELOG.md
└── pyproject.toml
```

## 模块职责

| 路径 | 职责 |
|------|------|
| `core/` | 可复现的系统模型：环境动力学、奖励、SATCPP/UAR 等领域创新 |
| `algo/` | 学习算法；arm 间共享除 satcpp/uar 外的超参 |
| `training/` | 训练循环、配置序列化、Run/Checkpoint、eval_suite |
| `experiments/` | CLI 入口、批量脚本调用的模块 |
| `figure/` | 读 metrics/checkpoint 产出 publication 图 |

## 配置驱动

- 单一 `ExperimentConfig`（dataclass + YAML）描述一次 arm 运行
- 每个 run 目录写入 **`config.yaml` 快照**（与 checkpoint 同级或 run 根）
- arm 间**仅** `satcpp` / `uar` / 骨干等创新维度不同，其余 held constant

## 与 uav-example 对照

| uav-example | 本规范 |
|-------------|--------|
| `runs_v1.2/<arm>/run_*` | 批次根 + arm + 时间戳 run |
| `src/training/run_manager.py` | RunManager 标准实现参考 |
| `src/training/checkpoint.py` | 三件套 + run_logs + dedup |
| `eval_suite_n200.json` | 批次级固定 hold-out |

新建项目时优先 **复制 uav-example 模式**，再按论文改 `core/` 与 arm 表。
