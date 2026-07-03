# tools/ 说明

## cnipa_epub_search.py

国知局公布公告站（epub.cnipa.gov.cn）检索，stdout 输出 `EPUB_HITS_JSON:`。

```bash
pip install -r requirements-cnipa.txt
python -m playwright install chromium
python3 cnipa_epub_search.py 检索词块
```

Agent 须**每轮一个词块**、多次调用后自行合并。详见 `prompts/search.md`。

## docx_to_md.py

Word → Markdown（含图片抽取到 `{name}_media/`）。

```bash
pip install mammoth  # 或 pip install -r ../requirements.txt
python3 docx_to_md.py --input in.docx --output out/in.md
```

## md_to_docx.py

Markdown → Word（A4 友好标题与段落）。

```bash
pip install python-docx
python3 md_to_docx.py --input in.md --output out.docx --base-dir .
```

推荐通过 `../scripts/render_disclosure_docx.py` 调用。

## iteration_dialog_log.py

每轮 merger / correction 交付后，在案件目录追加 `交底书修订对话记录.md`。

```bash
python3 iteration_dialog_log.py --case-dir outputs/某案件 --kind merge \
  --user "用户说明摘要" \
  --summary "合并摘要摘录" \
  --artifacts "案件名_20260703180530.md,案件名_20260703180530.docx"
```

`--kind correct` 用于纠正迭代。见 `prompts/iteration_context.md`。

## 来源

`cnipa_*`、`md_to_docx`、`docx_to_md`、`iteration_dialog_log.py` 改编自 [patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill)（MIT）。
