# Runs → 论文 Section V / 图表

与 **`paper-polish-skill`** 衔接：本 skill 产出**数据与 fig**；paper-polish 产出**表达与结构**。

## 数据流

```
runs_v1.x/<arm>/run_*/metrics.jsonl
        ↓
scripts/fig_*.py  (fig_comparison, fig_huot_curves, …)
        ↓
paper/section5_实验_v*.md  (数字 + Fig 引用)
        ↓
paper-polish-skill (experiment 模式 + code-abstraction)
        ↓
outputs/.../polished_*.md
```

## Fig 脚本约定

- 读 **批次内多 arm** 的 LATEST run 或指定 `run_id`
- 配色：本文方法 #E41A1C；见 paper-polish `figure-and-experiment.md`
- 输出到 `paper/` 或 `results/`；**同时**保留生成脚本与输入 metrics 路径于 section5 脚注

## section5 草稿最小结构

对齐 paper-polish **4 节标准版**：

```
V. PERFORMANCE EVALUATION
   A. Experimental Setup      ← Table I 来自 config.yaml + VERSION
   B. Convergence Analysis    ← metrics.jsonl 曲线
   C. Performance Comparison  ← 多 arm 主表
   D. Ablation and Insights   ← arm 对照即消融
```

## 交给 paper-polish 时提供

```markdown
## 交接包
- 代码版本：VERSION x.y.z
- 批次：runs_v1.2
- 主臂：qmix_tf_satcpp_uar
- 关键数字：HUOT x.xx（±），来源 metrics.jsonl ep=40000
- Fig 路径：results/fig_comparison.pdf
- 需润色：Section V 全文 + caption；**不要**写 train_kmappo() 等代码路径
```

## 版本对齐

- section5 文首注明：`Experiments use codebase v1.2.1, batch runs_v1.2.`
- 与 `CHANGELOG` 条目一致；数字变更时 bump section 文件名版本（如 `section5_实验_v1.2.1.md`）

## 禁止

- 手填数字无 metrics 行号/ep 来源
- 只交 png 不交 metrics/checkpoint
- 在 section5 正文写 `runs_v1.2/qmix_*/config.yaml` 路径（用 code-abstraction 改表述）
