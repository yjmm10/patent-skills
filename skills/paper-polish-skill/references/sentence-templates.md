# 万能句式模板库

润色时按需套用并替换占位符；避免整段模板化——同一段落最多 1–2 个模板句。

---

## 问题陈述

```
While [现有方法] achieve [优点], they fail to address [核心问题] in [本文场景], particularly when [具体条件].
```

```
However, significant research gaps persist: First, ... Second, ... Third, ...
```

```
Existing [任务] methods assume [不合理假设], which is unrealistic in [动态/灾害/边缘] scenarios where [具体条件].
```

---

## 方法创新

```
To this end, we propose [方法名], which [核心机制]. Unlike [对比方法], our approach [差异化优势].
```

```
We model [问题] as a [Dec-POMDP/MDP] where each [agent/UAV] [partial observability/动作空间描述].
```

```
Specifically, we [机制1], [机制2], and design [机制3] to [目标].
```

---

## 贡献声明

```
The main contributions of this article are summarized as follows:
1) We formulate ... as ..., capturing ...
2) We propose ... that addresses ...
3) We design ... to improve ...
4) Extensive simulations validate ... under ...
```

---

## 相关工作定位

```
Recent research on [主题] falls into three categories: 1) [类A] [refs]; 2) [类B] [refs]; 3) [类C] [refs].
```

```
However, these methods [共同局限], unlike [本文场景] where [动态特性].
```

```
To the best of our knowledge, this is the first work that combines [A] with [B] for [场景].
```

```
Differing from [ref], which focuses on [局限场景], our method addresses [本文场景] with [关键能力].
```

---

## 系统模型与问题

```
We consider a [场景] consisting of [节点列表]. Time is slotted with index t = 1, 2, ..., T.
```

```
Following [ref], we adopt the probabilistic LoS channel model ...
```

```
This formulation leads to a mixed-integer non-convex problem, which is NP-hard to solve optimally.
```

---

## 实验结果

```
Fig.X shows that [本文方法] outperforms [baseline] by [X]% in [指标], demonstrating the effectiveness of [创新点].
```

```
As illustrated in Fig.X, [方法] converges within [N] episodes, while [baseline] requires [M] episodes ([P]% slower).
```

```
Table X summarizes ... Our method achieves the best trade-off between [指标1] and [指标2].
```

```
The ablation study in Table X reveals that [组件] contributes most to [指标], as removing it degrades performance by [X]%.
```

---

## 局限与未来工作

```
Nevertheless, our approach has limitations. First, [局限1]. Second, [局限2]. These issues motivate future work on [方向].
```

```
In future work, we plan to: 1) [具体方向1]; 2) [具体方向2]; 3) [具体方向3].
```

---

## 章节过渡

```
The rest of this article is organized as follows. Section II reviews ... Section III presents ... Section IV details ... Section V evaluates ... Section VI concludes.
```

```
Having established the system model, we now present our proposed solution in Section IV.
```

```
Based on the problem formulation in Section III, we propose [方法名] in this section.
```

---

## 章节过渡（详见 section-transitions.md）

战略/战术/操作模板与案例见 **`references/section-transitions.md`**。以下为速查：

### 战略级（§ → §-A，约 3 句）

```
Having established the overall [系统] in Section [X], we now decompose...
Specifically, Section [X-A] details [子模块]...
This decomposition is essential because...
```

### 战术级（§-A → §-B，2–3 句）

```
The [主题] in Section [X-A] establishes...
However, ... alone is insufficient...
Therefore, Section [X-B] develops...
```

### 操作级（§-A → §-A1，1–2 句）

```
The [主题] comprises [N] components: ...
We begin with Section [X-A1], as it defines...
```

---

## 实验小节过渡（Section V 各节末句）

```
The baseline configurations and hyperparameters are summarized in Table I. In the following, we first examine the training convergence behavior.
```

```
These results confirm that [方法] converges faster and more stably than baselines, motivating the performance comparison under fully trained policies in the next subsection.
```

```
Having validated overall performance, we next isolate the contribution of each proposed component via ablation experiments.
```

```
In summary, the ablation results corroborate that [核心组件] is indispensable for [目标指标], while [次要组件] mainly affects [次要指标].
```

---

## 代码抽象化（详见 code-abstraction.md）

### 实现 / 训练框架（策略 5）

```
Implementation: Our framework is implemented using deep reinforcement learning libraries 
with [PyTorch/TensorFlow] backend. Multi-agent coordination employs [CTDE/parameter sharing]. 
Training was conducted on [GPU description]. Hyperparameters were tuned via [grid search/Bayesian optimization].
```

### 评估协议（策略 4）

```
Evaluation Protocol: We evaluate under [N] random seeds. Agents are trained for [M] episodes 
and tested over [K] episodes in unseen scenarios. Key metrics include [数学定义]. 
95% confidence intervals use Student's t-distribution. Implementation details are in Appendix [X]; 
code is available at [URL].
```

### 奖励 / 观测（策略 1）

```
The composite reward balances [objectives]: r_t = α·R_cov(·) − β·R_eng(·) + γ·R_smooth(·), 
where α, β, γ are tuned via grid search.
```

```
Raw observations undergo standardization: o = [(p − μ_p)/σ_p, OneHot(u_status)], 
where μ_p, σ_p are estimated from [N] random samples.
```

### 可复现性脚注（非正文）

```
Implementation details and hyperparameters are provided in Appendix [A/B]. 
Source code is available at [anonymized URL] for reproducibility.
```

---

## 图题（Caption）模板

```
Fig.X: [场景/设置]. [本文方法] achieves [量化结论] compared to [baseline(s)].
```

```
Fig.X: Convergence of [指标] versus training episodes for [算法列表]. Shaded areas denote 95% confidence intervals.
```

```
Fig.X: UAV trajectories in [场景]. Circles and crosses denote start and end points, respectively.
```
