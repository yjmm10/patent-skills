# 安装说明

本技能遵循 [AgentSkills](https://agentskills.io) 布局：**仓库根目录即技能根目录**，内含 `SKILL.md`。`name: patent-skills` 须与**文件夹名**一致。

## Claude Code

### 项目级（推荐协作）

```bash
mkdir -p .claude/skills
git clone <本仓库 URL> .claude/skills/patent-skills
```

### 用户级

```bash
mkdir -p ~/.claude/skills
git clone <本仓库 URL> ~/.claude/skills/patent-skills
```

运行时 `${SKILL_DIR}` 通常由环境设为技能目录（`CLAUDE_SKILL_DIR`）。

## Cursor

| 范围 | 路径 |
|------|------|
| 全局 | `~/.cursor/skills/patent-skills/` |
| 项目 | `<项目根>/.cursor/skills/patent-skills/` |

Windows PowerShell 示例：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills"
git clone <本仓库 URL> "$env:USERPROFILE\.cursor\skills\patent-skills"
```

重启 Cursor 后在 Settings → Rules 确认技能已加载，或使用 `/patent-skills`。

Cursor 亦扫描 `~/.claude/skills/` 与项目 `.claude/skills/`。

## Codex

```bash
git clone <本仓库 URL> patent-skills
cp -R patent-skills ~/.codex/skills/
```

`agents/openai.yaml` 提供 `$patent-skills` 快捷调用。

## 路径变量

| 变量 | 含义 |
|------|------|
| `${SKILL_DIR}` | 本文件所在目录（含 SKILL.md） |
| `CLAUDE_SKILL_DIR` | Claude Code 下的 `${SKILL_DIR}` |

命令示例中的 `${SKILL_DIR}` 请替换为实际安装路径，或由环境自动解析。

## 可选依赖

### DOCX 导出

```bash
pip install -r requirements.txt
```

### 国知局公布公告查新（Step search 优先路径）

```bash
pip install -r tools/requirements-cnipa.txt
python -m playwright install chromium
```

未安装时：

- 查新降级为 WebSearch / Google Patents
- 导出可仅交付 Markdown

### Word 输入

```bash
pip install -r requirements.txt
python3 tools/docx_to_md.py --input file.docx --output out/file.md
```

## 验证安装

1. 确认目录中存在 `SKILL.md`、`prompts/`、`references/`
2. 在 Agent 中说：「使用 patent-skills 评估一个测试创意的可专利性」
3. Agent 应 Read `prompts/review.md` 并按结构输出

## 打包分发

若已安装 [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator)：

```bash
python -m scripts.package_skill /path/to/patent-skills
```

生成 `.skill` 文件供离线安装。
