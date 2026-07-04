# 核心写作原则（贯穿全文润色）

## 逻辑连贯性

### 段落衔接

- 每段**首句**承接上段末句
- 每段**末句**引出下段
- 过渡词密度：每 100 词 2–3 个（However / Specifically / Consequently / To this end / In contrast）

### 章节衔接

- 章末预告：`Having established the system model, we now present our solution...`
- 章首回顾：`Based on the problem formulation in Section III, we propose...`

润色时：若段间跳跃，补 1 句过渡；若重复，删冗余保留一处。

---

## 技术表达

### 公式规范

- 符号首次定义：`where d is the distance (in meters)...`
- 重要公式单独成行、右对齐编号
- 避免连续 3 个以上公式无文字解释

### 算法描述

- 优先伪代码 over 长段 prose
- 必含 Input/Output 与复杂度

### 术语一致性

- 缩写：首次全称 (Full Name, FN)，此后 FN
- 不交替 UAV / drone
- convergence ≠ stability（按语境选用）

---

## 说服力增强

### 数据驱动

| 弱表述 | 强表述 |
|--------|--------|
| significant improvement | 23.6% improvement in throughput |
| fast convergence | converges 32% faster (1250 vs 1650 episodes) |
| always | typically / in most scenarios |
| outperforms all | outperforms MAPPO and MADDPG by X%–Y% |

无数据时：保留结构，标注 `[需作者补充: 相对 MAPPO 的吞吐量提升百分比]`

### 文献支撑

- 假设：`Following [21], we assume...`
- 对比：`Building upon [15]'s framework, we extend...`
- 不贬低前人：limitations / challenges / trade-offs

---

## AI 写作反模式（润色时删除或改写）

- 空洞开场：In recent years, with the rapid development of...
- 堆砌形容词：novel, innovative, groundbreaking 无具体机制支撑
- 对称废话段：每段长度完全一致、句式单一
- 过度破折号与 em dash
- 摘要/结论重复同一组数字超过两次

---

## 语言（中/英）

- **英文稿**：学术被动与主动平衡；Method 可用 we propose；Evaluation 用 results show
- **中文稿**：避免口语化；术语与英文缩写对照一致；图题中英期刊以用户要求为准

---

## 与作者协作

润色**不**擅自：

- 更改方法名称、算法步骤含义
- 虚构 baseline 名称或实验结果
- 删除作者明确保留的长公式（可建议移附录）

可**建议**：

- 缺失章节结构
- 需补充的实验维度
- 图题改写稿（单独列出）
