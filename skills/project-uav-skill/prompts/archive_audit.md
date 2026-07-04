# Archive Audit

**Read** `data-archival-contract.md`。

## 步骤

1. 解析 `runs/<batch>/<arm>/LATEST` → run 目录
2. Grep/Read 必存档清单每一项
3. 检查批次级 `eval_suite_n*.json`
4. 对照 VERSION/CHANGELOG 是否记录该批次
5. 给出等级 A/B/C/F + 修复命令建议

## 交付

使用 `data-archival-contract.md` 审计模板；列出缺失项与 **不重训可补** vs **必须重训** 项。
