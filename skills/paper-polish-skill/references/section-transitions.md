# 章节过渡写作指南：战略 / 战术 / 操作三级体系

> 过渡质量直接决定读者体验。本指南基于 IEEE IoT Journal、IEEE TNSM、Sensors 顶刊论文拆解。润色时：**章→子节**用战略级，**子节→子节**用战术级，**子节→小小节**用操作级。

## 目录

1. [黄金原则与效果标准](#黄金原则)
2. [战略级：章 → 子节](#战略级过渡)
3. [战术级：子节 → 子节](#战术级过渡)
4. [操作级：子节内部](#操作级过渡)
5. [信号词工具箱](#过渡信号词)
6. [常见错误与修正](#常见错误)
7. [期刊风格差异](#期刊过渡风格)
8. [完整演练示例](#实战演练)
9. [质量检查清单](#过渡质量检查清单)
10. [润色工作流与输出](#润色工作流)

---

## 黄金原则 {#黄金原则}

### 三级过渡体系

| 层级 | 范围 | 作用 |
|------|------|------|
| **战略级** | Section → Subsection（如 II → II-A） | 说明为何需要该子节；架构设计意图 |
| **战术级** | Subsection → Subsection（如 II-A → II-B） | 逻辑递进；让读者预见下文必要性 |
| **操作级** | Subsection → Subsubsection（如 II-A → II-A1） | 细化分解；技术细节展开顺序 |

### 效果标准

- **战略级**：读者理解章节架构的设计意图
- **战术级**：读者预见下文并理解其必要性
- **操作级**：读者明确技术细节的展开顺序

**润色优先级**：发现「断崖式过渡」（标题后直接正文、无承上启下）时，优先补战略级，再补战术/操作级。

---

## 战略级过渡 {#战略级过渡}

**结构**：3 句话 — **【承上】**回顾本章目标 + **【启下】**预告子节 + **【价值】**说明必要性

**篇幅**：约 3 句，60–90 词（IEEE IoT Journal 偏问题驱动，可至 90 词）

### 模板 1：分解式（最常用）

```
Having established the overall [系统/架构] in Section [X], we now decompose the system into its fundamental components. Specifically, Section [X-A] details the [子模块名], which serves as the foundation for [下游任务]. This decomposition is essential because [原因], as will be demonstrated in subsequent sections.
```

### 模板 2：问题驱动式

```
The [章名] presented in Section [X] reveals [N] core challenges: [挑战1], [挑战2], and [挑战3]. To address the first challenge, Section [X-A] develops a comprehensive [模型名] that captures [关键特性]. Understanding [X-A 主题] is prerequisite for [后续章/节目标].
```

### 模板 3：逻辑递进式

```
Section [X] introduced the system-level view of [场景]. Building on this foundation, Section [X-A] focuses on the [组件], which constitutes the basic operational unit of the entire system. This bottom-up approach enables us to first characterize component behavior before analyzing system-wide interactions in Sections [X-B]–[X-D].
```

### 真实案例（Guan — II → II-A）

```
Section II presented the overall system model for UAV-assisted disaster communications. To enable precise trajectory optimization, we first need accurate models of UAV dynamics and constraints. Accordingly, Section II-A develops a comprehensive UAV mobility model that incorporates both physical limitations (maximum speed, acceleration) and environmental factors (wind resistance, obstacle avoidance). This model forms the basis for our trajectory design framework in Section III.
```

---

## 战术级过渡 {#战术级过渡}

**结构**：2–3 句话 — **【总结】**本节核心结论 + **【连接】**与下节逻辑关系

**篇幅**：40–60 词；须含明确连接词（However / Therefore / Consequently）

### 模板 1：因果式

```
The [主题] in Section [X-A] establishes [结论/能力]. However, [能力] alone is insufficient for [任务]; we must also model [下节主题]. Therefore, Section [X-B] develops [模型/方法] that captures [关键特性].
```

### 模板 2：并列式

```
Section [X-A] characterized [物理/移动层], representing the [层名] of our system. Complementing this, Section [X-B] addresses the [通信/计算层] by modeling [行为]. Together, these two models provide the complete foundation for our optimization framework.
```

### 模板 3：问题-解决方案式

```
While Section [X-A] ensures [条件A], a critical question remains: [开放问题]? To answer this, Section [X-B] develops [模型] that accounts for [因素1], [因素2], and [因素3].
```

### 真实案例（Zhao — III-A → III-B）

```
The UAV mobility model in Section III-A defines how drones navigate maritime environments. Nevertheless, data collection requires not just movement but also reliable data transmission from sea surface to aerial nodes. Consequently, Section III-B introduces a cross-medium optical communication model that handles air-water interface refraction and turbulence effects. This communication model directly couples with mobility constraints to form our complete system representation.
```

### 与实验章 V-A → V-B 的战术级衔接

实验章各小节末句见 `experiment-section-structure.md`；战术级过渡同样适用（Setup → Convergence → Performance → Ablation）。

---

## 操作级过渡 {#操作级过渡}

**结构**：1–2 句话 — **【分解】**细化逻辑 + **【聚焦】**本小节目标

**篇幅**：20–30 词；主动语态（develops / presents / derives）

### 模板 1：组成式（最常用）

```
The [子节主题] comprises [N] interconnected components: [A] (Section [X-A1]), [B] (Section [X-A2]), and [C] (Section [X-A3]). We begin with [A] in Section [X-A1], as it defines the fundamental [约束/能力] that constrain all higher-level behaviors.
```

### 模板 2：重要性优先式

```
Among the various aspects of [主题], [Aspect1] are most critical for [目标]. Accordingly, Section [X-A1] first develops [内容], followed by [X-A2] and [X-A3]. This ordering reflects the dependency hierarchy where [依赖关系说明].
```

### 模板 3：数学推导式

```
To mathematically characterize [现象], we start from [基础理论] and derive simplified models suitable for optimization. Specifically, Section [X-A1] presents the [方程/模型] under [假设], which balance accuracy and computational tractability for our [RL/优化] framework.
```

### 真实案例（Ejaz — II-A → II-A1）

```
Section II-A established the UAV mobility framework at a high level. To enable precise trajectory planning, we now decompose this into mathematical models. Section II-A1 first derives the kinematic equations of motion, capturing position, velocity, and acceleration relationships. These equations serve as the foundation for energy modeling in Section II-A2 and obstacle avoidance in Section II-A3.
```

### 小小节正文开头（操作级 + 直入技术）

过渡段结束后，首句可立即进入模型（勿再重复过渡）：

```
The UAV kinematic model describes motion in 3D space using discrete time steps t = 1,2,...,T. We adopt the standard quadrotor dynamics from [21] but simplify for optimization tractability. Specifically, the position update follows: ...
```

---

## 过渡信号词 {#过渡信号词}

| 层级 | 常用信号词 |
|------|------------|
| **战略级** | Building on this foundation... / Extending this perspective... / Having established X, we now turn to Y... / Accordingly... |
| **战术级** | Complementing this... / However... / Nevertheless... / Consequently... / Therefore... / In parallel... |
| **操作级** | We begin with... / First... / Specifically... / More precisely... / At the core of this... / The most fundamental aspect... |

**密度参考**（非硬性上限，避免堆砌）：

| 期刊 | 风格 | 典型句长 | 信号词密度 |
|------|------|----------|------------|
| IEEE IoT Journal | 问题驱动 | 25–30 词/句 | 高（~3–4/100 词） |
| IEEE TNSM | 逻辑递进 | 20–25 词/句 | 中（~2–3/100 词） |
| Sensors | 应用导向 | 15–20 词/句 | 低（~1–2/100 词） |

润色时按用户 **目标 venue** 调整句长与信号词密度。

---

## 常见错误 {#常见错误}

| 错误类型 | 错误示例 | 修正 |
|----------|----------|------|
| **断崖式** | 标题 "Section 2.1 UAV Model" 后直接公式 | 标题下加 2–3 句战略/战术过渡 |
| **过度重复** | 重复 Section 2 内容超过 3 行 | 只提炼 1 句核心，快速进入新内容 |
| **逻辑跳跃** | UAV 模型直接跳到 reward 函数 | 加桥梁句：These mobility constraints directly influence our reward design in Section 3.2 |
| **被动堆砌** | The UAV model is presented in Section 2.1 | 主动：Section 2.1 **develops** the UAV mobility model |

---

## 期刊过渡风格 {#期刊过渡风格}

- **IEEE IoT Journal**：优先问题驱动式战略过渡；强调 challenge → subsection 对应
- **IEEE TNSM**：逻辑递进、bottom-up；Building on / Subsequently
- **Sensors**： shorter transitions；应用动机一句即可

---

## 实战演练 {#实战演练}

**场景**：Section 2 → 2.1 → 2.1.1（系统模型 → UAV 模型 → 运动学）

**2 → 2.1（战略级）**

```
Section 2 introduced the overall architecture of our cooperative UAV network for disaster communications. To enable rigorous mathematical optimization, we now decompose this system into its fundamental components, beginning with the UAV mobility model in Section 2.1. This focus is justified because UAV dynamics directly constrain trajectory design and ultimately determine communication coverage quality. Subsequent sections will build upon this foundation to model communication channels (Section 2.2) and energy systems (Section 2.3).
```

**2.1 → 2.1.1（战术级）**

```
Section 2.1 established UAVs as the core mobile nodes in our system. However, their operational capabilities are governed by physical laws that must be precisely modeled. Consequently, Section 2.1.1 develops the kinematic equations of motion, which capture position, velocity, and acceleration relationships under realistic constraints. These equations form the mathematical backbone for trajectory optimization in our proposed framework.
```

**2.1.1 正文开头（操作级后接技术）** — 见上文 Ejaz / 运动学示例。

---

## 过渡质量检查清单 {#过渡质量检查清单}

### 战略级

- [ ] 1 句总结上一章/节目标
- [ ] 明确本子节核心内容
- [ ] 解释对整体目标的必要性
- [ ] （推荐）预告后续子节关系

### 战术级

- [ ] 连接词标明逻辑（However / Therefore / Consequently）
- [ ] 2–3 句，约 40–60 词
- [ ] 不重复上节细节，聚焦新内容
- [ ] 建立与下节的技术依赖

### 操作级

- [ ] 说明分解逻辑（组成 / 重要性 / 推导）
- [ ] 明确本小节在子节中的定位
- [ ] 1–2 句，约 20–30 词
- [ ] 主动语态 + 明确动词（develops / presents / derives）

---

## 润色工作流 {#润色工作流}

### 四阶段（对齐作者写作流程）

1. **初稿**：内容先行；缺失过渡处标 `[TRANSITION NEEDED]`
2. **修改**：按战略 → 战术 → 操作顺序补过渡
3. **验证**：临时删除所有过渡段，检查是否仍能读懂；若不能，说明过渡必要
4. **优化**：删冗余句，确保每句有信息量

### Agent 润色流程

1. **扫描**：Grep 各 `\section`/`\subsection` 或 `##` 标题；检查标题下首段是否为「断崖」
2. **分级补写**：对每个边界选用对应模板（替换占位符，勿整段照搬）
3. **venue 微调**：按目标期刊调整句长与信号词密度
4. **桥梁句**：跨章跳跃（如 Model → Reward）单独补 1 句因果链

### 交付：过渡改进表（可选）

结构不合理或用户指定「只改过渡」时输出：

```markdown
## 过渡改进摘要

| 边界 | 级别 | 问题 | 处理方式 |
|------|------|------|----------|
| §II → II-A | 战略 | 断崖式 | 新增分解式过渡 3 句 |
| II-A → II-B | 战术 | 缺 However | 因果式过渡 2 句 |
| II-A → II-A1 | 操作 | 无 | 组成式 1 句 |

> 最佳过渡应「隐形」——引导自然，读者不觉被牵引；每句须承载信息，非填充。
```

---

## 与其他 reference 的衔接

- 章末/章首宏观衔接：`writing-principles.md` §章节衔接
- 实验小节末句：`experiment-section-structure.md` 各 V-A–V-D 末句模板
- 引言/贡献/结论句式：`sentence-templates.md`
