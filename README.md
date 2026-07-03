# Patent Skills

[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

**中国发明专利全流程 Agent Skill**：创意可专利性审核、论文/技术说明转专利、技术交底书撰写与迭代、国知局查新、A4 DOCX 导出、升级完整申请书。

技能包位于 **`skills/patent-skills/`**，符合 [AgentSkills](https://agentskills.io) 与 **CC Switch** 等工具的仓库扫描约定，可被 **Claude Code、Cursor、Codex** 等直接导入。

## 功能

| 模式 | 能力 |
|------|------|
| review | 创意/方案可专利性专家级初评 |
| convert | 论文/技术说明 → 专利素材，缺口结构化追问 |
| search | 国知局查新 + 现有技术对比 |
| draft | 交底书撰写（默认/自定义模板） |
| iterate | 合并/纠正、问答补充、**修订对话留痕** |
| export | A4 Markdown + DOCX |
| upgrade | 完整发明专利申请书五大部分 |
| standards | **联网 + 离线**专利法律与撰写规范约束 |

## 规范约束

- 离线基线：`skills/patent-skills/references/regulatory-standards.md`（专利法第 22/25/26 条、审查指南、国知局撰写提醒）
- 联网核验：`skills/patent-skills/prompts/standards_lookup.md`（review/draft/upgrade 前 WebSearch 权威来源）

## 快速安装

详见 [INSTALL.md](./INSTALL.md)。

```bash
# Claude Code / Cursor（复制技能子目录）
git clone <本仓库 URL> /tmp/patent-skills-repo
cp -R /tmp/patent-skills-repo/skills/patent-skills ~/.claude/skills/patent-skills

# CC Switch：仓库管理 → 添加仓库
# Owner: yjmm10  Name: patent-skills  Branch: master
# 刷新后即可发现 patent-skills 并一键安装
```

## 可选依赖

```bash
cd skills/patent-skills
pip install -r requirements.txt          # DOCX 导出
pip install -r tools/requirements-cnipa.txt && python -m playwright install chromium  # 国知局查新
```

未安装时自动降级（仅 MD / WebSearch 查新）。

## 使用示例

- 「评估这个方案能不能申请发明专利」
- 「把这篇论文转成技术交底书并查新」
- 「按默认模板写交底书，输出 Word」
- 「补充第三节实施例，并更新交底书」（自动另存时间戳版本 + 修订记录）
- 「生成完整发明专利申请书」

Codex：`$patent-skills` + 任务描述。

## 目录结构

```
patent-skills/                    # Git 仓库根
├── README.md
├── INSTALL.md
└── skills/
    └── patent-skills/            # 技能包（含 SKILL.md）
        ├── SKILL.md              # 主入口
        ├── agents/openai.yaml    # Codex 接口
        ├── prompts/              # 分模式指令
        ├── references/           # 专利规范与检查清单
        ├── assets/               # 默认交底书模板
        ├── scripts/              # DOCX 渲染
        └── tools/                # 查新、格式转换
```

## 致谢与参考

本 skill 在设计与实现上参考并融合了以下开源项目的思路与工具（均遵循各自许可证）：

- [paper2patent](https://github.com/7toCR/paper2patent) — 论文转专利规范与申请书结构
- [patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill) — 交底书流程与国知局查新脚本
- [cn-patent-disclosure-writing-skill](https://github.com/cycloneha/cn-patent-disclosure-writing-skill) — 模块化交底书写作与合规
- [PatentRadar](https://github.com/yuc16/PatentRadar) — 专利检索与对比方法论（侵权分析未纳入 v1）

## 免责声明

本工具输出仅供技术整理与撰写参考，不构成法律意见或正式专利申请文件。专利申请、权利要求布局及侵权风险评估须由具备资质的专利代理师或律师审核。

## License

MIT — 见 [LICENSE](./LICENSE)
