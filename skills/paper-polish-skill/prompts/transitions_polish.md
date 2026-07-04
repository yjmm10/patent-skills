# Step 3c: Transitions — 章节过渡专项润色

**Read** `references/section-transitions.md`；全文上下文可选 **Read** `references/writing-principles.md`。

## 适用场景

- 用户明确要求：过渡、衔接、section transition、承上启下
- diagnose 发现大量断崖式过渡
- full 润色中的过渡子任务（不重复改全文技术内容）

## 执行步骤

1. **扫描边界**：列出所有 Section → Subsection、Subsection → Subsection、Subsection → Subsubsection 标题对
2. **分级标注**：每对标记 战略 / 战术 / 操作；标注 断崖 / 重复 / 跳跃 / 被动
3. **按 venue 选模板**：见 section-transitions.md「期刊过渡风格」
4. **补写或改写**：替换 `[TRANSITION NEEDED]`；标题下插入过渡段（战略/战术 2–3 句，操作 1–2 句）
5. **跨章桥梁**：Model ↔ Method、Method ↔ Reward 等跨章跳跃须 1 句因果链
6. **验证**：过渡段每句有信息量；不重复上节超过 1 句核心

## 输出

```markdown
## 过渡润色结果

### [边界标识，如 §II → II-A]
**级别**：战略级
**润色后过渡段**：
（英文/中文正文）

---

## 过渡改进摘要
| 边界 | 级别 | 问题 | 处理 |
|------|------|------|------|

## 检查清单（section-transitions.md）
- 战略级：✅/⚠️/❌ × N
- 战术级：...
- 操作级：...
```

## 禁止

- 不改动公式、算法、实验数值（仅过渡段与边界相邻 1 句）
- 不整段机械套用模板；须填入本文具体术语与章节编号
