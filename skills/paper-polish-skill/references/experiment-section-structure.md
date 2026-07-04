# 实验部分标准章节结构（3–5 小节）

> 基于 IEEE IoT Journal、IEEE TNSM、Sensors 四篇顶刊论文拆解。实验章占全文 **25–30%**（12 页稿约 3–4 页）；每小节 **300–400 词**；全章 **5–8 个核心图表**；逻辑顺序：**设置 → 训练过程 → 最终性能 → 深入分析**。

---

## 三种标准划分

### 3 节精简版（10–12 页）

```
V. PERFORMANCE EVALUATION
   A. Simulation Setup and Baselines
   B. Performance Comparison and Analysis
   C. Ablation Study and Discussion
```

| 项 | 说明 |
|----|------|
| 适用 | 创新点集中、实验维度较少；单一 RL 算法改进 |
| 代表 | Ejaz 等 — RL-Planner (IEEE TNSM, 2024) |
| 注意 | 收敛性须并入 B 节首段 + 独立 Fig.，不可与设置混写 |

### 4 节标准版（12–15 页，**推荐默认**）

```
V. SIMULATION RESULTS AND ANALYSIS
   A. Experimental Setup
   B. Convergence Analysis
   C. Performance Comparison
   D. Ablation Study and Insights
```

| 项 | 说明 |
|----|------|
| 适用 | 核心创新明确、需全面验证；K-means+MAPPO 类改进 |
| 代表 | Guan 等 — KMAPPO (IEEE IoT Journal, 2024) |
| 优势 | 收敛单独成节突出训练特性；消融独立强化创新说服力 |

### 5 节全面版（15+ 页）

```
V. PERFORMANCE EVALUATION
   A. Simulation Environment and Parameters
   B. Convergence and Training Analysis
   C. Comprehensive Performance Comparison
   D. Scalability and Parameter Sensitivity
   E. Case Studies and Visualization
```

| 项 | 说明 |
|----|------|
| 适用 | 多算法协同系统；大量场景验证；重要轨迹/可视化 |
| 代表 | Zhao 等 — MECOS (IEEE IoT Journal, 2026)；Zhu 等 — LLM-QTRAN（跨域 LLM+MARL，4–5 节） |

---

## 章节数量决策指南

| 论文特征 | 推荐节数 | 案例 |
|----------|----------|------|
| 单一创新点，标准 RL 算法改进 | **3 节** | Ejaz RL-Planner（单 UAV 路径规划） |
| 核心创新明确，需全面验证 | **4 节** | Guan KMAPPO（K-means + MAPPO） |
| 多算法协同，系统级方案 | **5 节** | Zhao MECOS（LMAR2P + MAPBal） |
| 跨领域创新（LLM + MARL 等） | **4–5 节** | Zhu LLM-QTRAN |

**润色时**：若用户未指定，根据全文页数、创新点数量、是否多算法/多场景，**推荐**一种划分并在变更摘要说明理由；不强行拆/合导致内容重复。

---

## 六维验证 ↔ 小节映射

「六维」是**内容覆盖**维度；映射到 3/4/5 节时按下列规则，避免节数与内容脱节：

| 六维内容 | 3 节版 | 4 节版 | 5 节版 |
|----------|--------|--------|--------|
| 实验设置 / baselines / 指标 | **A** | **A** | **A** |
| 收敛性 | B 开篇 + Fig. | **B** | **B** |
| 性能对比 | **B** | **C** | **C** |
| 规模扩展性 | B 末段或 C 前段 | C 中多场景子段 | **D** |
| 参数敏感性 | C 讨论段 | C 末段或脚注 | **D** |
| 消融实验 | **C** | **D** | D 末段或并入 C |
| 场景适应 / 可视化 | B/C 穿插 | C 多场景 + 1 图 | **E** |

---

## 4 节标准版：各小节内容规范

### V-A: Experimental Setup（~0.5 页，300–400 词）

**必备四块**：

1. **环境配置**：仿真工具（PyTorch/MATLAB）、硬件平台、随机种子
2. **关键参数表**：Table I，至少 3 列（Parameter / Value / Description）
3. **对比基线**：3–5 个算法 + **选择理由**（代表性/多样性/公平性/进展性，见 `figure-and-experiment.md`）
4. **评估指标**：4–6 个，分效能 / 效率 / 鲁棒性三类

**小节末句模板**：`The baseline configurations and hyperparameters are summarized in Table I. In the following, we first examine the training convergence behavior.`

**图表**：Table I（必须）；可选 Fig. 仿真区域示意图

---

### V-B: Convergence Analysis（~0.75 页，300–400 词）

**必备**：

- 同环境下多算法收敛曲线（Fig.4 典型）
- **关键观察**：收敛速度、最终性能、稳定性（方差/置信区间）
- 可选：学习率、折扣因子等超参数敏感性（4 节版可 1 段 + 1 子图；深度敏感放 5 节 D）

**图表**：≥1 曲线图，本文方法 #E41A1C 实线 + 置信区间

**小节末句模板**：`These results confirm that [方法] converges faster and more stably than baselines, motivating the performance comparison under fully trained policies in the next subsection.`

---

### V-C: Performance Comparison（~1 页，350–400 词）

**必备**：

- 标准指标上与全部 baseline 的主结果（Table / Fig.5）
- **多维度验证**：不同场景 / 规模 / 条件（至少 2 种）
- **统计显著性**：标准差、置信区间；有 p-value 则标注
- **机制解释**：1–2 句说明为何本文更好（对应 Method 中创新点）

**图表**：≥1 柱状/折线对比图；可选多场景子图

**小节末句模板**：`Having validated overall performance, we next isolate the contribution of each proposed component via ablation experiments.`

---

### V-D: Ablation Study and Insights（~0.75 页，300–400 词）

**必备**：

- **消融设计**：逐个移除创新组件的变体（勿组合移除混淆归因）
- **量化影响**：性能下降百分比（Table V 模板见 `figure-and-experiment.md`）
- **Key Insight**：哪一组件贡献最大及原因
- **限制分析**：1 段说明何种条件下方法优势减弱或失效

**图表**：消融表或柱状图；可选 1 个 failure/limitation 场景图

**小节末句模板**：`In summary, the ablation results corroborate that [核心组件] is indispensable for [目标指标], while [次要组件] mainly affects [次要指标].`

---

## 3 节 / 5 节版差异要点

### 3 节版合并规则

| 小节 | 吸收内容 |
|------|----------|
| A | 同 4 节 A |
| B | 4 节 B 收敛段 + 4 节 C 主对比 + 多场景；**B 内须分两段标题或加粗引导**（Convergence / Main Results） |
| C | 4 节 D 消融 + 讨论 + 局限性 |

**禁止**：将 Setup 与 Convergence 合并为一节（审稿人易质疑训练稳定性）。

### 5 节版扩展规则

| 小节 | 扩展内容 |
|------|----------|
| D | 用户规模 + UAV 数量等 **Scalability**；学习率/clip/环境参数 **Sensitivity**（合并为一节，勿各参数单独成节） |
| E | 典型场景 case study、轨迹/热力图可视化、极端条件测试 |

---

## 常见错误与修正

| 错误 | 问题 | 修正 |
|------|------|------|
| **<3 节** | 设置与结果/analysis 混为一节 | 至少拆分 Setup vs Results |
| **>6 节** | 每个参数单独成节，琐碎 | 合并为 Scalability and Parameter Sensitivity |
| **逻辑倒置** | 先展示结果再说明设置 | 严格 A→B→C→D |
| **收敛并入对比无 Fig.** | 审稿人质疑训练 fairness | 3 节版也须独立 convergence 图/段 |
| **无小节过渡句** | 故事线断裂 | 每小节末 1 句承上启下 |

---

## 顶刊经验法则（润色实验章时对照）

- **图表密度**：每小节 ≥1 核心图/表；全章 5–8 图
- **文字精炼**：描述趋势与机制，数字放图表；正文引用 `Fig.X` / `Table X`
- **故事线**：读者仅读 Section V 应能理解方法优势
- **自检三问**（diagnose / experiment 模式输出可选附）：
  1. 新读者能否仅通过实验部分理解优势？
  2. 每个图表是否证明核心贡献？
  3. 消融是否无可辩驳地证明创新点必要性？

> *"Reviewers spend 40% of their time on the experimental section. Make every graph count, and every number tell a story."* — IEEE TMC 编辑建议

---

## 润色输出：实验章结构建议表

当实验章小节划分不合理时，除正文外输出：

```markdown
## 实验章结构建议

| 项 | 当前 | 建议 | 理由 |
|----|------|------|------|
| 节数 | 2 节 | 4 节标准版 | 12 页稿 + 独立 MAPPO 改进，需单独收敛节 |
| V-A | 缺失独立 Setup | 拆分 Table I + baselines | 设置与结果分离 |
| V-B | （无） | 新增 Convergence Analysis | 避免与性能对比合并 |
| … | … | … | … |

### 建议目录
V. SIMULATION RESULTS AND ANALYSIS
   A. ...
   B. ...
```

若仅润色措辞、结构已合理，可省略此表。
