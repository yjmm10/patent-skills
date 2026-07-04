# 代码与实现细节抽象化指南

> 正文描述**为什么**和**是什么**，而非**怎么做**。实现细节属于附录/开源仓库。审稿人视角：*"If I can see your file paths, I'm reading engineering documentation, not scientific contribution."*

## 目录

1. [论文 vs 代码文档](#本质区别)
2. [五层抽象策略](#五层抽象策略)
3. [高危细节规避清单](#高危规避清单)
4. [实战转换模板](#实战转换模板)
5. [润色工作流与输出](#润色工作流)
6. [投稿前检查清单](#投稿前检查清单)

---

## 本质区别 {#本质区别}

| 特征 | 学术论文 | 代码文档 |
|------|----------|----------|
| 目标 | 贡献通用知识 | 指导具体实现 |
| 受众 | 领域专家（未必懂你的代码） | 开发者 |
| 持久性 | 5–10 年仍有价值 | 随代码更新失效 |
| 抽象层次 | 理论 / 方法 / 洞见 | 实现 / 接口 / 参数 |
| 评估标准 | 创新性、严谨性 | 正确性、效率 |

**润色准则**：保留科学含义，剥离工程暴露面；超参数**数值**可留正文，**来源代码位置**不可留。

---

## 五层抽象策略 {#五层抽象策略}

润色时对每处代码痕迹选用对应层级转换。

### 策略 1：函数 → 数学操作

| 代码痕迹 | 论文表达 |
|----------|----------|
| `uav_pos`, `user_pos` | \(\mathbf{p}_i\), \(\mathbf{u}_j\) |
| `np.linalg.norm(...)` | Euclidean distance \(d_{ij}\) |
| 硬编码常数 32.4, 0.3 | 引用标准模型文献，正文只保留符号 |
| 函数名 `calculate_channel_gain` | "channel gain is modeled as" + 公式 |

**转换技巧**：数学符号替代变量名；引用标准模型（"follows the probabilistic LoS model from [21]"）；多行合并为单个表达式；隐藏非贡献性常数细节。

**示范**

```
The channel gain between UAV i and user j is modeled as Eq. (X), where d_{ij} is the 
Euclidean distance, P_LoS follows the probabilistic LoS model from [21], and κ 
represents the NLoS attenuation factor.
```

---

### 策略 2：类 / 模块 → 系统组件

| 代码痕迹 | 论文表达 |
|----------|----------|
| `class UAVAgent` | "Each UAV i ∈ 𝒩 is modeled as an autonomous agent" |
| `self.position`, `self.energy` | state \(\mathbf{s}_i = [\mathbf{p}_i, e_i, \mathbf{c}_i]\) |
| `MAX_ENERGY` | maximum energy capacity \(E_{\max}\)（符号，非常量名） |
| `step()` 内更新逻辑 | 动力学方程 \( \mathbf{p}_i(t+1) = ... \), \( e_i(t+1) = ... \) |

**转换技巧**：集合/状态向量替代 OOP 属性；公式替代计算逻辑；引用领域文献（aerodynamics literature）；初始化细节移附录。

---

### 策略 3：算法流程 → 伪代码 / 数学描述

| 代码痕迹 | 论文表达 |
|----------|----------|
| `train_kmapppo()`, `for episode in range` | **Algorithm 1** 标准伪代码（Input/Output/步骤） |
| `UPDATE_INTERVAL` | update interval \(\tau\) |
| `agent.select_action` | \(a_i^t \sim \pi_i(o_i^t)\) |
| 自定义训练函数名 | "Proximal Policy Optimization [ref]" + 目标期望 |

**伪代码规范**：Algorithm 1 标题；Input/Output；与 `chapter-guidelines` Method 章一致；**不出现** Python 语法、`def`、`import`。

**数学描述备选**：最大化期望累积回报 + 引用 PPO/MARL 经典算法名。

---

### 策略 4：实验脚本 → 评估协议

| 代码痕迹 | 论文表达 |
|----------|----------|
| `config_path="configs/disaster_scenario.yaml"` | "disaster communication scenarios" / "simulation parameters in Table I" |
| `results['throughput']` | Average throughput 数学定义 + 单位 |
| `save_results("results/kmapppo_final.pkl")` | 删除；可选脚注 "Code available at [URL]" |
| `for seed in range(50)` | "50 random seeds"; 95% CI via Student's t-distribution |

**转换技巧**：指标用数学定义；说明统计方法而非循环；配置细节 → Table I 或 Appendix A；`evaluate(..., episodes=100)` → "tested over 100 episodes in unseen scenarios"。

---

### 策略 5：技术栈 → 方法论

| 代码痕迹 | 论文表达 |
|----------|----------|
| `torch==1.12.0`, `ray[rllib]==1.11.0` | "deep reinforcement learning framework with PyTorch backend" |
| 具体 GPU 型号（可保留概括） | "NVIDIA GPU with 24GB memory" 或 Table I 一行 |
| 库列表 | CTDE 范式、parameter sharing、Bayesian hyperparameter tuning |

**正文避免**：版本号、`pip install`、requirements.txt 内容。

**附录可写**：关键超参数表（无代码格式）；环境文字描述（非 YAML）。

---

## 高危规避清单 {#高危规避清单}

### 正文绝对避免

| 代码细节 | 替代方案 |
|----------|----------|
| 文件路径 `configs/xxx.yaml` | "configuration parameters" / Table I |
| 函数名 `calculate_flight_energy()` | "energy consumption model" |
| 库版本 `torch==1.12.0` | "deep learning framework" |
| 变量名 `MAX_ENERGY = 10000` | \(E_{\max}\) |
| 类名 `class UAVAgent:` | "UAV agent model" |
| 注释 `# TODO` | 删除 |
| `print(...)` 调试 | 删除 |
| 绝对路径 `/home/user/...` | 删除 |

### 附录 / 脚注可谨慎出现

- 关键超参数表（Appendix A）
- 环境配置文字描述（Appendix B，非 YAML）
- Algorithm 1 伪代码（正文，标准格式）
- 开源链接（脚注/致谢）
- 硬件概括（实验 Setup 节）

---

## 实战转换模板 {#实战转换模板}

### 模板 1：奖励函数

**代码**：`reward = alpha * coverage_reward - beta * energy_penalty + gamma * smoothness_reward`

**论文**：

```
The composite reward function balances three objectives:
r_t = α·R_cov(s_t) − β·R_eng(a_t) + γ·R_smooth(a_t, a_{t−1})
where α=0.6, β=0.3, γ=0.1 are weighting coefficients tuned via grid search to 
prioritize coverage while maintaining energy efficiency and trajectory smoothness.
```

### 模板 2：超参数扫描

**代码**：`for lr in [0.001, 0.0005, 0.0001]: for gamma in [0.95, 0.99]: run_experiment(...)`

**论文**：

```
Hyperparameter Sensitivity: We analyze learning rate α ∈ {10^{−3}, 5×10^{−4}, 10^{−4}} 
and discount factor γ ∈ {0.95, 0.99}. As shown in Fig. 7, α=10^{−3} and γ=0.99 
achieve the optimal trade-off between convergence speed and final performance.
```

### 模板 3：观测预处理

**代码**：`preprocess_observation(raw_obs)` with normalize + one-hot

**论文**：

```
Observation Processing: Raw observations o^raw undergo standardization:
o = [(p − μ_p)/σ_p, OneHot(u_status)]
where μ_p and σ_p are computed over 10,000 random environment samples.
```

### 错误 vs 正确对照

**错误（退稿级）**

```
We implemented the controller in uav_controller.py using PyTorch 1.8.1. 
train_kmapppo() loads configs/disaster_config.yaml and saves to ./results/experiment_1/. 
Our reward function in reward.py uses alpha=0.6 as defined in line 42.
```

**正确（录用级）**

```
Training Framework: Our implementation employs deep reinforcement learning with 
parameter sharing among homogeneous UAVs. The reward function balances coverage, 
energy, and smoothness with weights α=0.6, β=0.3, γ=0.1 from sensitivity analysis. 
Training details and hyperparameters are in Appendix B; code is at [URL] for reproducibility.
```

---

## 润色工作流 {#润色工作流}

### 四阶段

1. **扫描**：Grep 正文中的路径、`def `、`.py`、`import`、`torch`、`yaml`、`class `、`` ` `` 代码块、行号引用
2. **分级转换**：对每处应用五层策略之一
3. **验证三问**（每处保留/删除前）：
   - 是否证明科学贡献，而非仅展示实现？
   - 5 年后库变更后是否仍可读？
   - 未用过 Python 的领域专家能否理解？
4. **附录分流**：无法删除的技术细节 → 建议 `[移至 Appendix A: …]`

### Agent 交付：代码抽象改进表

```markdown
## 代码抽象改进摘要

| 位置 | 原表述（问题） | 润色后 | 策略 |
|------|----------------|--------|------|
| §IV ¶2 | uav_controller.py | Training framework employs... | 策略5 |
| §IV | train_kmapppo() | Algorithm 1 / PPO training | 策略3 |
| §V-A | configs/disaster.yaml | Table I parameters | 策略4 |

### 建议附录条目（可选）
- Appendix A: Hyperparameter table
- Appendix B: Implementation notes (no file paths)
```

### 术语对照表（建议放附录）

| 代码术语 | 论文术语 |
|----------|----------|
| MAX_SPEED | \(v_{\max}\) |
| energy_model() | Energy consumption model |
| train_kmapppo() | KMAPPO training procedure (Algorithm 1) |

---

## 投稿前检查清单 {#投稿前检查清单}

- [ ] 正文无文件路径（含相对路径）
- [ ] 无具体函数名/类名/模块名（用 "our method" / "the proposed algorithm"）
- [ ] 无库版本号
- [ ] 无调试/TODO/print 残留
- [ ] 变量用数学符号；算法用 Algorithm 1 伪代码
- [ ] 实现细节在附录或脚注；代码链在致谢/脚注
- [ ] 内联代码块已改为公式或 prose（Method/Model 章重点）

---

## 与其他 reference 的衔接

- Method 章伪代码格式：`chapter-guidelines.md` §Proposed Method
- 实验 Setup 指标定义：`figure-and-experiment.md` §Evaluation Protocol
- 反模式（AI 堆砌）：`writing-principles.md`
