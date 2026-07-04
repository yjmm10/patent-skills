# Step 3a: Full Polish — 全文逐章润色

**Read** `references/chapter-guidelines.md`、`references/writing-principles.md`、**`references/section-transitions.md`**、**`references/code-abstraction.md`**（Method/Evaluation）；实验章 **Read** `experiment-section-structure.md` + `figure-and-experiment.md`；句式 **Read** `sentence-templates.md`。

## 润色顺序（按 ROI 排序）

审稿人平均 20 分钟；**前 3 页与前 3 图**优先：

1. **Title + Keywords**
2. **Abstract**（强制五句公式）
3. **Introduction**（五段式 + 贡献列表）
4. **Related Work**（三步法）
5. **System Model**（四层 + 符号定义）
6. **Proposed Method**（四步 + 伪代码/Reward；**应用 code-abstraction 策略 1–3**）
7. **Performance Evaluation**（3/4/5 小节；**策略 4–5** 处理实验脚本与技术栈表述）
8. **Conclusion**（三段式）

References 仅做格式/一致性提示，不重写文献内容。

## 每章润色流程

```
1. 对照 chapter-guidelines 该节「检查清单」
2. 保留技术含义，调整结构与句式
3. 检查 Section→Subsection 边界：按 section-transitions 补战略/战术/操作过渡
4. 补量化表述、Fig./Table 引用；实验小节末过渡句见 experiment-section-structure
5. Method/Evaluation：扫描并抽象化代码痕迹（code-abstraction 五层策略）
6. 记录变更到 Change Log
```

## 标注规则

- 默认：重大改动句末加 `【润色】` 或行内 `[polished]`
- 用户要求「干净终稿」：交付无标注版 + 单独 Change Log
- 缺数据：`[需作者补充: 具体说明]`

## 输出结构

```markdown
# [论文标题] — 润色稿

## Title
...

## Abstract
...

## I. Introduction
...

（各章完整正文）

---

## 变更摘要
| 章节 | 主要改动 | 依据 |
|------|----------|------|

## 检查清单得分
（简表 ✅/⚠️/❌）
```

## 保存

写入 `./outputs/{论文标识}/polished_{YYYYMMDDHHmmss}.md`（若可写）。

## 禁止

- 不更改算法/公式数学含义（可改符号说明清晰度）
- 不删除作者实验数值
- 交付正文不含 self_check 全文
