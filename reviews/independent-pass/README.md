# 独立逐段复审

开始日期：2026-10-22（Asia/Shanghai）。本目录记录本次独立检查；原有 `reviews/` 报告保留，不能作为本次已完成的证据。

## 起点与工作区保护

- 仓库：`D:\code\system-design\fundamentals-zh`；上级目录不是 Git 仓库。
- 起始提交：`782fd96c738577637e86faefdd5ebcff6720c2d4`。
- 起始 `git status --short`：仅 `?? .idea/`。没有已跟踪文件的未提交修改；不读取、修改、暂存或提交 `.idea/`。
- 已检查上级路径及工程内的 `AGENTS.md`，未发现；已读 `translation-guide.md`、README 和现有前言记录以了解结构，不继承旧完成结论。
- 按原书顺序逐段审校；本地按章提交，明确列出暂存路径，不推送。

## 原书身份

- 依据 PDF 第 5 页正文扉页、第 6 页版权／修订历史、7–14 页目录核实，而非仅依据封面或文件名。
- 书名：*Fundamentals of Software Architecture: An Engineering Approach*；作者：Mark Richards、Neal Ford；出版社：O’Reilly。
- 第一版（February 2020），所用文件含第四次发布修订（2021-02-12），不是第二版。ISBN：978-1-492-04345-4。正文仍按第一版出版语境翻译，不用当前产品状态改写。
- PDF 共 422 页。页序从 1 起算；前言 xiii–xvii = PDF 15–19；正文／附录／索引的阿拉伯页码加 20 = PDF 页序；分部扉页另见范围表。
- PDF 第 20 页为空白；第 1 章从 PDF 21 / 书内 1 页开始。第一部分位于第 1 章之后，按书中顺序处理。
- 只读 PDF，未修改源文件；提取及渲染缓存放在忽略的 `tmp/independent-pass/`。页面图像用于核对排版、图表、公式和提取疑点。

## 范围与证据

范围清单见 [scope.md](scope.md)，批次与断点见 [progress.md](progress.md)，未决事项见 [open-questions.md](open-questions.md)。每个单元的报告从英文段落起句、标题、图表等建立覆盖关系；已有 HTML 编号仅作译稿定位，不作为原文段落计数。

每个完成单元均须完成英文对照、中文连续通读、实质修改回查及附件检查。自动检查只验证结构。全书一致性检查须在所有范围逐段完成后单独进行。
