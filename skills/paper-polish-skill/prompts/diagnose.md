# Step 2: Diagnose — 全文结构诊断

**Read** `references/final-checklist.md`、`references/chapter-guidelines.md` 后执行；实验章 **Read** `experiment-section-structure.md`；过渡 **Read** `section-transitions.md`；代码暴露 **Read** `code-abstraction.md`。

## 目标

不改正文，输出优先级排序的问题清单，供用户确认后进入润色。

## 诊断步骤

1. **章节映射**：列出稿件现有章节 vs 标准结构（Title, Abstract, I–VI, References）
2. **逐章快扫**（每章 3–5 条 bullet）：
   - 结构是否符合该章「标准骨架」（见 chapter-guidelines）
   - 是否缺量化数据、缺过渡、术语不一致
   - 图表引用是否支撑主张
4. **实验章小节诊断**（有 Section V 时）：
   - 统计现有子节数量（A/B/C…）；对照 3/4/5 节标准，**推荐**目标划分
   - 检查逻辑顺序：Setup 是否在 Results 之前；收敛是否独立 Fig./小节
   - 检查常见错误：<3 节、>6 节、设置与结果合并、缺消融独立节
   - 输出「建议目录」草案（可放入诊断报告 P1）
5. **过渡诊断**（扫描 Section/Subsection 标题）：
   - 断崖式：标题下直接公式/正文、无承上启下
   - 逻辑跳跃：如 Model 直跳 Reward 无桥梁句
   - 过度重复：过渡段复述上节 >3 行
   - 输出 P1c「过渡问题表」（边界 / 级别 / 问题类型）
6. **代码暴露诊断**（Grep `.py`, `configs/`, `def `, 库版本）：
   - 文件路径、函数/类名、内联代码块、requirements 版本
   - 输出 P1d「代码抽象问题表」（位置 / 类型 / 建议策略 1–5）
7. **跑 final-checklist**：统计 ✅/⚠️/❌
8. **DNA 五要素**：一贡献、两核心图、三类对比、四数值、五层逻辑

## 输出格式

使用 `references/final-checklist.md` 末尾的「诊断报告输出格式」。

## 交互

- 若有 **P0 缺失**（如无 Abstract、无 Evaluation、方法章空白）：询问用户是否先补内容再润色
- **diagnose 模式**：交付诊断报告后**停止**，除非用户要求继续润色
- **full 模式**：展示诊断摘要（可折叠详细项），默认继续 Step 3

## 禁止

- 不在诊断阶段大段重写正文
- 不虚构问题；无实验数据则标「缺数据」而非编造
