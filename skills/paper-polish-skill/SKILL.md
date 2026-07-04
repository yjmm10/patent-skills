---
name: paper-polish-skill
description: >-
  工程类学术论文润色：顶刊框架、实验章3-5小节、三级过渡、代码/实现细节抽象化（路径/函数名/库版本→公式与伪代码）。用户提到论文去代码化、实现细节太多、file path in paper、把代码改成数学描述、伪代码、附录分流时均应使用本技能。
version: "1.4.0"
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

- 明确提及：润色论文、章节过渡、**代码抽象化**、去代码化、实现细节、file path、函数名进正文
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
| `experiment` | 实验章 3–5 小节 + 图表 caption | `section_polish.md` + `experiment-section-structure.md` + `figure-and-experiment.md` |
| `transitions` | 章/子节过渡专项 | `transitions_polish.md` + `section-transitions.md` |
| `code_abstraction` | 代码/路径/库版本 → 理论表达 | `code_abstraction_polish.md` + `code-abstraction.md` |

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
| **`references/experiment-section-structure.md`** | **润色/诊断实验章；决定 3/4/5 节划分与各小节内容** |
| `references/figure-and-experiment.md` | 图表样式、Table I、baseline、六维内容映射 |
| `references/writing-principles.md` | 段落衔接、公式与术语；宏观章际一句式 |
| **`references/section-transitions.md`** | **战略/战术/操作三级过渡；模板、案例、断崖修正** |
| `references/sentence-templates.md` | 贡献、实验、结论句式；过渡详见 section-transitions |
| **`references/code-abstraction.md`** | **五层抽象策略；路径/函数/技术栈规避；Method/Evaluation 去代码化** |
| `references/final-checklist.md` | diagnose 与 self_check 阶段 |

---

## 润色原则（贯穿全文）

1. **保真创新**：不改变技术贡献含义；只优化表达、结构与说服力。
2. **数据驱动**：把模糊词（"significant improvement"）替换为可量化表述；无数据则标注待补。
3. **结构优先于辞藻**：先对齐章节骨架（倒金字塔引言、五句摘要、实验章 3–5 小节等），再修句法。
4. **术语一致**：全文统一缩写（首次全称）；不混用 UAV/drone 等同义词。
5. **图表自解释**：图题含关键结论；正文点名 Fig.X 支撑的主张。
6. **过渡如神经系统**：见 `section-transitions.md`。
7. **代码抽象化**：正文写贡献不写仓库；路径/函数名/库版本 → 公式、伪代码、评估协议（见 `code-abstraction.md`）。
8. **尊重期刊体例**：IEEE/Elsevier 等以用户指定模板为准。

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
| Step 3c | `prompts/transitions_polish.md` | 章节过渡专项 |
| Step 3d | `prompts/code_abstraction_polish.md` | 代码与实现细节抽象化 |
| Step 4 | `prompts/self_check.md` | 交付前内部自检 |
| 迭代 | `prompts/iteration.md` | 基于上轮结果的增量修改 |

**禁止**：在交付正文中包含「自检清单」全文；自检仅内部使用。

---

## 版本管理

**当前版本**：见 frontmatter `version` 与 **`CHANGELOG.md`** 最新条目。

每次修改本 skill（`SKILL.md`、`prompts/`、`references/`、`evals/`）**必须**：

1. **递增版本号**（`SKILL.md` frontmatter `version`）
2. **写入 `CHANGELOG.md`**：新版本号、日期、`Added` / `Changed` / `Fixed` / `Removed` 摘要
3. **向用户说明**：回复中注明「paper-polish-skill vX.Y.Z」及本次变更要点

### 版本号规则

|  bump  | 场景 |
|--------|------|
| PATCH (+0.0.1) | 措辞修正、typo、检查项微调 |
| MINOR (+0.1.0) | 新 reference / 新模式 / 新 prompt / 显著能力扩展 |
| MAJOR (+1.0.0) |  breaking：删除或重命名模式、重构主流程 |

### Changelog 条目模板

```markdown
## [X.Y.Z] — YYYY-MM-DD

### Added
- ...

### Changed
- ...

### Fixed
- ...
```
