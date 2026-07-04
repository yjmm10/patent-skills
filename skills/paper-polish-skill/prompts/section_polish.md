# Step 3b: Section Polish — 单章节润色

**Read** `references/chapter-guidelines.md` 对应节；实验/图表 **Read** `references/figure-and-experiment.md`。

## 章节 → 规范映射

| 用户指定 | 应用规范 |
|----------|----------|
| title, 标题 | Title 三种公式 + 检查清单 |
| abstract, 摘要 | 五句公式 |
| introduction, 引言 | 五段式 + 贡献模板 |
| related work, 相关工作 | 三步法 |
| system model, 模型, formulation | 四层递进 |
| method, proposed, 方法 | 四步结构 |
| experiment, evaluation, 实验 | 六维 + figure-and-experiment |
| conclusion, 结论 | 三段式 |
| caption, 图题 | figure-and-experiment 自解释原则 |

未指定时询问一章名称。

## 流程

1. 只润色指定章节（± 相邻 1 句过渡若明显断裂）
2. 输出：**润色后章节全文** + **变更摘要** + **该章检查清单**
3. 若该章依赖他章术语（如 Method 引用 Section III 公式编号），保持一致，必要时提示作者统一

## 特殊：front 模式

仅 Title + Abstract + Keywords；Abstract 严格五句；提供 2–3 个备选标题（三种公式各一，若适用）。

## 特殊：experiment 模式

除正文外，可选输出：

- 建议的 Table I 参数表（Markdown）
- 图题改写列表
- 缺失的六维中哪几维未覆盖

## 输出示例

```markdown
## 润色：Abstract

（润色后全文）

### 本段变更
- 句 2：问题陈述加强 dynamic disaster 对比
- 句 5：补充 32% / 18.7% 与正文 Fig.5 一致

### 章节检查清单
- ✅ 5 句结构
- ⚠️ 句 4 机制名可再具体
```
