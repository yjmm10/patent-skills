# Step 1: Intake — 输入收集

执行本步前无需其他 prompt。

## 目标

确定工作模式、收集润色所需上下文，避免盲目改稿。

## 必问/必确认项

从用户消息与附件中提取；缺失项**最多追问 3 个**（合并成一条消息）：

| 项 | 说明 | 默认 |
|----|------|------|
| 稿件来源 | 文件路径 / 粘贴文本 / 上轮输出 | — |
| 工作模式 | full / section / diagnose / front / experiment | 有全文→full；仅一段→section |
| 目标语言 | 英文 / 中文 | 以稿件主语言为准 |
| 目标 venue | 期刊或会议名（如 IEEE IoT Journal） | 通用 IEEE 工程体例 |
| 领域标签 | 如 MARL+UAV+MEC | 通信/优化工程类 |
| 润色侧重 | 逻辑 / 数据量化 / 术语 / 图表 caption / 全面 | 全面 |

## 模式判定规则

- 用户说「只改摘要」「润色 introduction」→ **section** 或 **front**
- 用户说「帮我看看有什么问题」「诊断一下」→ **diagnose**
- 用户说「实验部分」「图题」→ **experiment**
- 用户在上轮润色稿上提修改 → **iteration**（改读 `iteration.md`）
- 用户要从零写论文 → **停止**，建议 `academic-paper`

## 读取稿件

1. 若 `.tex` / `.md` / `.docx`：Read 或转换后 Read
2. 大文件：先 Grep 章节标题，再分段 Read
3. 记录：总章节列表、缺失章节、明显语言混用

## 输出（简短确认）

```markdown
## 润色任务确认
- 模式：full
- 语言：English
- 目标：IEEE IoT Journal 风格
- 范围：全文 8 节
- 侧重：摘要五句公式 + 引言贡献条 + 实验量化
- 稿件：[路径或「用户粘贴」]

开始诊断 / 开始润色 [章节名]。
```

确认后进入下一步：**diagnose**（full/diagnose）或 **section_polish**（section/front/experiment）。
