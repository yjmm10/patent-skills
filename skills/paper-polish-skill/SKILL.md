---
name: paper-polish-skill
description: >-
  工程类学术论文润色与表达优化：基于顶刊论文拆解的写作框架，按章节（标题/摘要/引言/相关工作/系统模型/方法/实验/结论）结构化润色现有初稿，强化逻辑连贯、数据说服力与图表自解释性。特别适配 MARL、UAV 网络优化、边缘计算等方向，框架通用。用户提到润色论文、改进表达、优化摘要引言、工程论文写作规范、顶刊写作框架、论文检查清单、图表规范、实验章节润色时均应使用本技能。区别于 academic-paper（从零撰写全流程），本技能专注已有稿件的表达层优化。
version: "1.0.0"
user-invocable: true
argument-hint: "[可选：论文章节或文件路径，如 abstract / introduction / 全文]"
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, Bash
---

# 工程类学术论文润色

**核心理念：好论文 = 30% 创新 + 70% 表达。**

本技能针对**已有初稿**进行结构化润色，不替代研究创新本身。分步指令在 **`prompts/`**，章节规范在 **`references/`**——执行对应步骤前 **`Read`** 相应文件。

## 与 `academic-paper` 的分工

| 场景 | 使用技能 |
|------|----------|
| 从零写论文、文献检索、完整 12-agent 流水线 | `academic-paper` |
| **已有初稿，优化表达、结构、说服力** | **本技能** |
| 审稿意见回复、rebuttal | `academic-paper`（revision-coach 模式） |
| 结构化 peer review 打分 | `academic-paper-reviewer` |

---

## 触发条件

- 明确提及：润色论文、改进论文表达、优化摘要/引言、论文写作规范、顶刊写作框架、论文检查清单
- 英文：polish paper, improve academic writing, revise abstract/introduction, engineering paper structure
- 斜杠指令：`/paper-polish`、`/润色论文`
- **迭代模式**：用户在上轮润色结果上继续改（改某段、加强数据、统一术语等）→ **`Read`** `prompts/iteration.md`，**不**默认重跑全文诊断

**不触发**：用户要从零写新论文 → 路由到 `academic-paper`。

---

## 工作模式

根据用户意图选择模式；未说明时，有完整稿件用 **full**，只给某章节用 **section**，只要诊断报告用 **diagnose**。

| 模式 | 适用场景 | 主要 Prompt |
|------|----------|-------------|
| `full` | 全文润色 | `intake.md` → `diagnose.md` → `full_polish.md` → `self_check.md` |
| `section` | 单章节润色 | `intake.md` → `section_polish.md` → `self_check.md` |
| `diagnose` | 只出诊断报告，不改文 | `intake.md` → `diagnose.md` |
| `front` | 标题 + 摘要 + 关键词 | `intake.md` → `section_polish.md`（限定 Title/Abstract） |
| `experiment` | 实验章节 + 图表说明/ caption | `intake.md` → `section_polish.md`（Evaluation）+ `references/figure-and-experiment.md` |

---

## 主流程（full 模式）

1. **`Read`** `prompts/intake.md` → 收集：稿件路径/粘贴内容、目标期刊或会议、语言（中/英）、领域标签、润色侧重（逻辑/数据/术语/图表说明）
2. **`Read`** `prompts/diagnose.md` → 对照 `references/final-checklist.md` 输出**诊断报告**（章节完整性、结构合规、主要问题清单，按优先级排序）
3. 向用户展示诊断摘要；若问题涉及缺失实验/数据，**先询问**是否补充再继续润色
4. **`Read`** `prompts/full_polish.md` + 对应章节 **`references/chapter-guidelines.md`** → 逐章润色
5. **`Read`** `prompts/self_check.md` → 内部自检（**不写入交付正文**）
6. 交付物见下节

**section 模式**：跳过步骤 2 的全文诊断，改为对该章节执行 `section_polish.md` 中对应小节规则。

---

## 交付格式

每次交付须包含：

### 1. 润色后正文

- 保留原有章节标题与公式编号体系；改动处用 **`【润色】`** 或 diff 风格标注（用户要求「直接给终稿」时可去掉标注）
- 不捏造实验数据、不虚构引用；缺失数据处标注 `[需作者补充: …]`

### 2. 变更摘要（Change Log）

```markdown
## 变更摘要
| 章节 | 主要改动 | 依据规则 |
|------|----------|----------|
| Abstract | 重构为 5 句公式 | chapter-guidelines §Abstract |
| … | … | … |
```

### 3. 检查清单得分

对照 `references/final-checklist.md`，给出 ✅/⚠️/❌ 及一句说明（内部自检详细项不展开给用户，除非用户要求）。

### 4. 保存路径（有文件写入权限时）

```
./outputs/{论文标识}/polished_{YYYYMMDDHHmmss}.md
```

---

## Reference 文件索引

| 文件 | 何时 Read |
|------|-----------|
| `references/chapter-guidelines.md` | 润色任一正文章节前 |
| `references/figure-and-experiment.md` | 润色 Evaluation、图题、表题、实验设计描述 |
| `references/writing-principles.md` | 全文逻辑衔接、公式与术语统一 |
| `references/sentence-templates.md` | 需要改写问题陈述、贡献声明、局限/未来工作 |
| `references/final-checklist.md` | diagnose 与 self_check 阶段 |

---

## 润色原则（贯穿全文）

1. **保真创新**：不改变技术贡献含义；只优化表达、结构与说服力。
2. **数据驱动**：把模糊词（"significant improvement"）替换为可量化表述；无数据则标注待补。
3. **结构优先于辞藻**：先对齐章节骨架（倒金字塔引言、五句摘要、六维实验等），再修句法。
4. **术语一致**：全文统一缩写（首次全称）；不混用 UAV/drone 等同义词。
5. **图表自解释**：图题含关键结论；正文不重复图题全部内容，但要点名 Fig.X 支撑的主张。
6. **尊重期刊体例**：IEEE/Elsevier 等格式细节以用户指定模板为准；本技能不强制改 LaTeX 宏包。

---

## 领域适配

默认参考域：**多智能体强化学习 + UAV 网络优化 + 边缘计算**。其他工程类论文（通信、物联网、优化、联邦学习等）同样适用章节框架；领域专有术语保留作者原意，仅修正表达。

---

## Prompt 文件映射

| 步骤 | 文件 | 用途 |
|------|------|------|
| Step 1 | `prompts/intake.md` | 输入收集与模式判定 |
| Step 2 | `prompts/diagnose.md` | 全文结构诊断 |
| Step 3a | `prompts/full_polish.md` | 全文逐章润色顺序与输出要求 |
| Step 3b | `prompts/section_polish.md` | 单章节润色 |
| Step 4 | `prompts/self_check.md` | 交付前内部自检 |
| 迭代 | `prompts/iteration.md` | 基于上轮结果的增量修改 |

**禁止**：在交付正文中包含「自检清单」全文；自检仅内部使用。
