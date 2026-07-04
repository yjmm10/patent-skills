# 各章节撰写与润色指南

> 基于 IEEE IoT Journal、IEEE TNSM、Sensors 等顶刊论文拆解。12 页标准论文篇幅分配见下表。

## 标准章节结构与篇幅

| 章节 | 页数（12页稿） | 重点 | 核心技巧 |
|------|----------------|------|----------|
| 标题+摘要 | 0.5 | 精准定位 | 5 句公式 + 4 关键词 |
| Introduction | 1.5 | 建立坐标 | 倒金字塔 + 3 条贡献 |
| Related Work | 1 | 证明必要性 | 分类→对比→定位 |
| System Model | 2 | 可复现基础 | 四层递进 + Fig.1 锚定 |
| Proposed Method | 3 | 核心创新 | 问题转化→算法→复杂度 |
| Performance Evaluation | 3 | 说服审稿人 | 六维验证 + 消融 |
| Conclusion | 0.5 | 闭环升华 | 贡献→局限→未来 |

---

## 标题 (Title)

**原则**：信息密度最大化——问题/场景 + 方法 + 核心技术。

### 三种标题公式（任选其一）

1. **[方法] for [场景/问题]: A [核心技术] Approach**
2. **[核心技术]-Enhanced [方法] for [场景]**
3. **[缩写]: [场景] Leveraging [技术1] and [技术2]**

### 案例

| 公式 | 案例 |
|------|------|
| 1 | Cooperative UAV Trajectory Design for Disaster Area Emergency Communications: A Multiagent PPO Method |
| 2 | Task Offloading with LLM-Enhanced Multi-Agent Reinforcement Learning in UAV-Assisted Edge Computing |
| 3 | MECOS: Cooperative Multi-UAV-Assisted Cross-Boundary Maritime Data Collection Leveraging MARL and LLM |

### 润色检查清单

- [ ] 12–15 个英文单词（中文标题对应 20–30 字）
- [ ] 含至少一个可检索技术关键词（MARL/DRL/LLM/UAV 等）
- [ ] 避免 "A Novel Approach to..."
- [ ] 含领域关键词

---

## 摘要 (Abstract) — 150–250 词

**原则**：独立成文；问题→方法→验证闭环。

### 五句公式（严格顺序）

| 句序 | 功能 | 模板 | 字数 |
|------|------|------|------|
| 1 | 背景定位 | With the advancement of... | 20–25 词 |
| 2 | 问题陈述 | However.../Nevertheless... | 25–30 词 |
| 3 | 方法概述 | This paper proposes... | 30–35 词 |
| 4 | 技术创新 | Specifically... | 25–30 词 |
| 5 | 效果验证 | Simulations/experiments demonstrate... | 20–25 词 |

### 示范

> With the advancement of 5G/6G communications, rapid deployment of emergency networks in disaster areas has become critical. However, traditional infrastructure is often damaged, and existing UAV solutions suffer from slow convergence in dynamic environments. This paper proposes KMAPPO, a K-means accelerated multi-agent proximal policy optimization framework for cooperative UAV trajectory design. Specifically, we transform the problem into a decentralized POMDP, leverage K-means clustering for initial trajectory seeding, and design a novel reward function balancing coverage and energy efficiency. Simulations demonstrate that KMAPPO achieves 32% faster convergence and 18.7% higher throughput compared to state-of-the-art baselines under various disaster scenarios.

### 润色检查清单

- [ ] 5 句对应 5 功能
- [ ] 含 2–3 个具体数值
- [ ] 无文献引用；缩写首次写全称
- [ ] 4–5 个领域关键词

---

## 引言 (Introduction) — 1.5 页

**原则**：漏斗式——时代背景 → 场景 → 挑战 → 方案 → 贡献 → 结构。

### 五段式结构

| 段落 | 字数 | 内容 |
|------|------|------|
| 1 宏观背景 | ~150 | 6G/万物智联趋势；UAV 等节点的重要性 |
| 2 场景聚焦 | ~200 | 具体场景；现有方案及局限（静态/单智能体/忽略动态性） |
| 3 问题定义 | ~250 | 3–4 个 research gap；技术层面分析为何现有方案不足 |
| 4 本文方案 | ~300 | 方法名；3–4 条编号贡献 |
| 5 论文结构 | ~100 | The rest of this article is organized as follows... |

### 贡献声明模板

```
The main contributions of this article are summarized as follows:
1) We formulate ... as a Dec-POMDP problem, capturing ...
2) We propose a novel [技术名称] that addresses ...
3) We design [具体机制] to improve ...
4) Extensive simulations validate ... under [场景]
```

### 润色要点

- 每条贡献对应一个 research gap
- 段落 3 可量化现有方案不足（"only achieves 45% coverage"）
- 每 100 词 2–3 个逻辑连接词（However/Specifically/To this end/In contrast）
- **不写**方法细节（留给 Method 章）

---

## 相关工作 (Related Work) — 1 页

**原则**：建立学术坐标，非文献堆砌。

### 三步法

1. **分类**（~150 词）：按技术路线/场景/时间分 2–3 类，每类 2–3 篇代表工作
2. **对比**（~200 词）：每类核心缺陷；与本文场景的不匹配
3. **定位**（~100 词）：与现有工作的本质区别；To the best of our knowledge...

### 关键句式

- 分类：Recent research on ... falls into three categories: 1) ... 2) ... 3) ...
- 对比：However, these methods assume static environments, unlike ...
- 定位：Differing from these studies, our ... framework leverages ...

### 润色检查清单

- [ ] 每类 3–5 篇权威引用
- [ ] 每类末尾 In contrast/Unlike/Differing from
- [ ] 用 limitations 而非 failures 描述前人工作
- [ ] 末句明确本文定位

---

## 系统模型与问题建模 — 2 页

**原则**：审稿人可复现；四层递进。

| 层 | 内容 | 篇幅 |
|----|------|------|
| Layer 1 场景描述 | 拓扑、坐标、假设；**Fig.1 系统图** | ~300 词 |
| Layer 2 信道模型 | LoS、路径损耗、速率公式 | ~250 词 + 3–4 式 |
| Layer 3 行为模型 | 移动性、能量、计算/卸载 | ~350 词 + 2–3 式 |
| Layer 4 问题建模 | 变量、目标、约束；标注 NP-hard/non-convex | ~200 词 |

### 润色要点

- Fig.1 仅为场景图，无算法细节
- **Section II → II-A 等边界**：按 `section-transitions.md` 补战略级过渡（分解式/问题驱动）
- **II-A → II-B**：战术级因果或并列过渡（mobility → channel）
- 每个符号首次出现定义（where θ is ...）
- 优化问题标注复杂度
- 可选：Table of Notations；3–5 条假设列表
- 模型选择引用文献（Following [21], we adopt...）

---

## 提出的方法 — 3–4 页

**结构**：问题转化 → 算法架构 → 关键模块 → 复杂度。

| 步骤 | 内容 |
|------|------|
| Step 1 问题转化 | 转为 MDP/Dec-POMDP；五元组 G = ⟨S,A,P,r,Ω,O,N,γ⟩ |
| Step 2 算法架构 | **Fig.2** 输入-处理-输出；CTDE/分布式；创新点标红 |
| Step 3 关键模块 | State/Obs、**Reward**（重点）、网络结构、训练技巧；伪代码 |
| Step 4 复杂度 | 时间/空间复杂度；与 baseline 对比 |

### Reward 示范结构

```
r_t = α·R_coverage + β·R_energy + γ·R_smooth
```
每项须有物理意义；系数来源（grid search 等）说明。

### 伪代码要求

- Algorithm 1 标题；Input / Output；关键步骤含探索、存储、更新
- **禁止** Python/`def`/文件路径；见 `code-abstraction.md` 策略 3

### 代码痕迹抽象化（Method 章必查）

- 类/Agent → 状态空间与动力学公式（策略 2）
- 函数/脚本 → 数学操作或 Algorithm 1（策略 1、3）
- 保留 α、β、episode 数等科学参数；删除 `reward.py`、`line 42` 等工程指称

---

## 性能评估 — 3–4 页（全文 25–30%）

**小节结构（3–5 节）**：润色前 **`Read`** `references/experiment-section-structure.md`。

| 版式 | 页数 | 小节 |
|------|------|------|
| 3 节精简 | 10–12 页 | A Setup+Baselines → B Performance+Convergence → C Ablation+Discussion |
| **4 节标准（默认推荐）** | 12–15 页 | A Setup → B Convergence → C Performance → D Ablation+Insights |
| 5 节全面 | 15+ 页 | A Environment → B Convergence → C Performance → D Scalability+Sensitivity → E Case Studies |

**逻辑顺序**：设置 → 训练过程 → 最终性能 → 深入分析（禁止先结果后设置）。

**内容六维**（映射到小节，见 experiment-section-structure.md）：收敛、性能对比、规模扩展、参数敏感、消融、场景适应。

### 润色要点

- 根据创新点复杂度**推荐 3/4/5 节划分**；每小节 300–400 词，末句过渡下节
- 每小节 ≥1 核心图/表；全章 5–8 图
- 每个主张对应 Fig./Table；量化对比（23.6% lower AoI）
- Table I 仿真参数（Setup 节）；消融独立成节（4/5 节版为 D）

---

## 结论 — 0.5 页

**三段式**：贡献总结 → 局限承认 → 未来方向。

| 段 | 字数 | 内容 |
|----|------|------|
| 1 | ~200 | 重述问题与方案；强调技术洞察（非重复摘要数字） |
| 2 | ~100 | 2–3 个具体局限；学术诚实 |
| 3 | ~150 | 2–3 个可行未来方向；与局限对应 |

### 禁止

- 引入新概念/新缩写
- 局限否定方法核心价值
- 空泛 future work（"improve performance"）

---

## 好论文 DNA（润色时对照）

- **一个**核心贡献贯穿全文
- **两张**核心图：Fig.1/2 架构 + Fig.5 关键结果
- **三类**对比：经典 / SOTA / 消融
- **四个**关键数值：摘要与结论必有量化提升
- **五层**逻辑递进：段首承接、段末引出
