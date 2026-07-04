# 图表规范与实验设计

> **实验章小节划分**（3/4/5 节标准、各节篇幅、决策指南、常见错误）→ **`Read`** `experiment-section-structure.md`。本文档侧重图表样式、Table I、baseline 与六维**内容**要点。

## 图类型与小节对应（4 节标准版）

| 图号 | 类型 | 功能 | 典型小节 |
|------|------|------|----------|
| Fig.1 | 系统架构图 | 场景认知 | System Model（非实验章） |
| Fig.2 | 算法架构图 | 方法核心 | Method |
| Table I | 仿真参数 | 可复现设置 | **V-A Setup** |
| Fig.4 | 收敛曲线 | 训练稳定性 | **V-B Convergence** |
| Fig.5 | 性能对比 | 主结果 | **V-C Performance** |
| Fig.6+ | 消融/扩展/轨迹 | 深入分析 | **V-D Ablation** 或 **V-E Case** |

## 图类型与功能对应（全稿）

| 图号 | 类型 | 功能 | 出现位置 |
|------|------|------|----------|
| Fig.1 | 系统架构图 | 场景认知：节点+链路+覆盖 | System Model 开头 |
| Fig.2 | 算法架构图 | 方法核心：输入-处理-输出，标红创新点 | Method 开头 |
| Fig.3 | 流程/时序图 | 运行逻辑 | Method 中部 |
| Fig.4–5 | 收敛/性能对比 | 证明有效；本文红色实线+置信区间 | Evaluation 开头 |
| Fig.6+ | 敏感/消融/轨迹 | 深入分析 | Evaluation 后半 |

---

## 配色与样式

### 曲线图

| 元素 | 规范 |
|------|------|
| 本文方法 | #E41A1C 红色实线，线宽 2.5pt |
| Baseline1 | #377EB8 蓝色虚线 |
| Baseline2 | #4DAF4A 绿色点线 |
| Baseline3 | #984EA3 紫色点划线 |
| 置信区间 | 半透明填充 alpha=0.2 |
| 字体 | Arial 10pt；图例右上角 |

### 柱状图

| 元素 | 规范 |
|------|------|
| 本文方法 | #E41A1C 纯色 |
| Baseline | 蓝/绿/紫 + 不同填充纹理 |
| 误差棒 | 黑色 capsize=5 |
| 数值标签 | 柱顶上方 2pt，Arial 8pt |

### 轨迹可视化

- UAV 轨迹：红/蓝/绿实线
- 起点 ○（5pt）；终点 ×（1.5pt）
- 障碍物：黑色粗线或填充矩形
- 风险区：红色虚线等高线 alpha=0.3

---

## 图表自解释原则

润色 **caption 与正文引用** 时确保：

1. **标题含结论**：`Fig.5: KMAPPO achieves 32% faster convergence than MAPPO under 80 users`
2. **坐标轴带单位**：`Training Episode (×10³)` 而非裸 `Episode`
3. **图例完整**：`KMAPPO (Ours)` 而非仅 `Ours`
4. **关键点标注**：曲线上标拐点（`Optimal point: η=0.6`）

正文句式：`Fig.X shows that [方法] outperforms baselines by [X]% in [指标], demonstrating ...`

---

## 实验设置透明化

### Table I: Simulation Parameters（必备）

| Parameter | Value | Description |
|-----------|-------|-------------|
| Area size | 1000×1000 m² | Simulation area |
| UAV count | 5 | Number of UAVs |
| Learning rate | 0.001 | Adam optimizer |
| ... | ... | ... |

### 环境细节（正文或脚注）

- 仿真：**方法论表述**（"deep RL framework with PyTorch backend"），**非** `torch==1.12.0`
- 硬件：GPU 型号、内存（Table I 或 Setup 一句）
- 随机种子：如 50 runs with different seeds
- 代码：脚注/致谢 `[URL]`；配置细节 → Appendix（见 `code-abstraction.md`）

---

## Baseline 选择四原则

1. **代表性**：至少 1 篇近三年顶会/顶刊方法
2. **多样性**：传统优化 + 学习-based
3. **公平性**：相同设置与指标
4. **进展性**：经典到 SOTA

推荐组合：1×经典（Q-learning/PSO）+ 2×SOTA（MAPPO/MADDPG）+ 1×启发式（Greedy/Auction）

---

## 评估指标三维度

| 维度 | 示例指标 |
|------|----------|
| 效能 | 吞吐量、延迟、成功率、AoI |
| 效率 | 收敛速度、计算时间、通信开销 |
| 鲁棒性 | 标准差、最坏情况 |

所有对比须含标准差或置信区间。

---

## 六维验证内容（按 4 节标准版映射）

润色时先确定小节划分（见 `experiment-section-structure.md`），再确保六维**内容**覆盖：

### 维度 1：收敛性 → V-B

- 多算法同环境收敛曲线
- 指标：收敛速度、最终性能
- 本文方法红色实线 + 置信区间

### 维度 2：性能对比 → V-C

- 3–5 baselines；4–5 指标
- 案例句：KMAPPO achieves 23.6% lower AoI and 18.7% higher throughput than MAPPO...

### 维度 3：规模扩展性 → V-C 子段或 V-D（5 节版）

- UAV 数量、用户密度扫描
- 关键句：scales linearly ... while PSO degrades quadratically

### 维度 4：参数敏感性 → V-B 简要或 V-D（5 节版）

- 学习率、折扣因子、clip；或环境参数（能见度等）
- 可用热力图展示二维参数

### 维度 5：消融实验 → V-C（3 节版）或 V-D（4/5 节版）

Table V 模板：

| Variant | Description | Convergence (Episodes) | Throughput (Mbps) |
|---------|-------------|------------------------|-------------------|
| Full | Complete method | 1250 | 45.6 |
| w/o K-means | Remove clustering init | 1650 (-32%) | 38.2 (-16.2%) |
| w/o R_smooth | Remove smoothness reward | 1320 (-5.6%) | 42.1 (-7.7%) |

Key Insight 一句总结各组件贡献。

### 维度 6：场景适应性 → V-C 多场景或 V-E（5 节版）

- 3+ 场景（城市/郊区/海上/灾害）
- 极端条件；轨迹可视化

---

## 实验设计速查（润色时纠正常见错误）

| 实验类型 | 必备元素 | 常见错误 |
|----------|----------|----------|
| 收敛性 | 5+ 算法，足够 episode，置信区间 | 无方差、episode 不足 |
| 性能对比 | 3–5 baselines，4+ 指标，显著性 | baseline 不合理、指标单一 |
| 消融 | 单组件移除、量化影响 | 组合移除、未证必要性 |
| 参数敏感 | 参数扫描、最优值标注 | 范围不合理、无物理意义 |
| 场景适应 | 3+ 场景、极端测试 | 场景过于理想 |

---

## 润色 experiment 章节时的输出

除正文外，可附 **图表改进建议表**（若用户仅给文字未给图文件）：

```markdown
| 图号 | 当前问题 | 建议修改 |
|------|----------|----------|
| Fig.4 | 缺置信区间 | 添加 shaded CI；本文用红色实线 |
| Fig.5 caption | 仅描述内容无结论 | 改为 "... achieves X% improvement ..." |
```
