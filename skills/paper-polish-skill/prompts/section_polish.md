# Step 3b: Section Polish — 单章节润色

**Read** `references/chapter-guidelines.md` 对应节；实验/图表 **Read** `references/experiment-section-structure.md` + `references/figure-and-experiment.md`。

## 章节 → 规范映射

| 用户指定 | 应用规范 |
|----------|----------|
| title, 标题 | Title 三种公式 + 检查清单 |
| abstract, 摘要 | 五句公式 |
| introduction, 引言 | 五段式 + 贡献模板 |
| related work, 相关工作 | 三步法 |
| system model, 模型, formulation | 四层递进 |
| method, proposed, 方法 | 四步结构 |
| experiment, evaluation, 实验 | **3–5 小节结构** + 六维内容 + figure-and-experiment |
| conclusion, 结论 | 三段式 |
| transition, 过渡, 衔接 | transitions 模式 |
| code, 代码, 路径, 函数名, 去代码化 | **code_abstraction** 模式 |

未指定时询问一章名称。

## 流程

1. 只润色指定章节（± 相邻 1 句过渡若明显断裂）
2. 输出：**润色后章节全文** + **变更摘要** + **该章检查清单**
3. 若该章依赖他章术语（如 Method 引用 Section III 公式编号），保持一致，必要时提示作者统一

## 特殊：front 模式

仅 Title + Abstract + Keywords；Abstract 严格五句；提供 2–3 个备选标题（三种公式各一，若适用）。

## 特殊：experiment 模式

**必读** `experiment-section-structure.md`。

1. **结构评估**：根据全文页数与创新点，推荐 3/4/5 节版；若当前划分不合规，输出「实验章结构建议表」与建议目录
2. **逐小节润色**（4 节标准版默认）：A Setup → B Convergence → C Performance → D Ablation；每节 300–400 词，**末句 1 条过渡**
3. **内容覆盖**：对照六维映射，标注缺失维度（规模/敏感/场景等）
4. **附加输出**（按需）：
   - Table I 参数表（Markdown）
   - 图题改写列表（自解释 + 含结论）
   - 顶刊自检三问（结构合理时可省略）

## 特殊：code_abstraction 模式

改读 **`prompts/code_abstraction_polish.md`**，不执行本节单章流程。

## 特殊：transitions 模式

改读 **`prompts/transitions_polish.md`**，不执行本节单章流程。

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
