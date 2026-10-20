# 《软件架构基础》中文翻译与学习笔记

基于 Mark Richards、Neal Ford 的 *Fundamentals of Software Architecture: An Engineering Approach*（英文第一版，2020）。本工程用于个人学习，译文与学习笔记分别维护。

## 阅读进度

| 章节 | 译稿 | 学习笔记 | 进度 |
| --- | --- | --- | --- |
| 第 1 章 引言 | [译稿](chapters/01-introduction/translation.md) | [笔记](chapters/01-introduction/notes.md) | 全文已翻译并校订（书内第 1–20 页）；含 7 幅原图及中文标签对照 |
| 第 2 章 架构思维 | [译稿](chapters/02-architectural-thinking/translation.md) | [笔记](chapters/02-architectural-thinking/notes.md) | 全文已翻译并校订（书内第 23–36 页）；含 9 幅原图、表 2-1 及中文标签对照 |
| 第 3 章 模块化 | [译稿](chapters/03-modularity/translation.md) | [笔记](chapters/03-modularity/notes.md) | 全文已翻译并校订（书内第 37–53 页）；含 6 幅原图、5 个公式及中文标签对照 |
| 第 4 章 架构特性的定义 | [译稿](chapters/04-architecture-characteristics-defined/translation.md) | [笔记](chapters/04-architecture-characteristics-defined/notes.md) | 全文已翻译并校订（书内第 55–64 页）；含 2 幅原图、3 张表及中文标签对照 |
| 第 5 章 识别架构特性 | [译稿](chapters/05-identifying-architectural-characteristics/translation.md) | [笔记](chapters/05-identifying-architectural-characteristics/notes.md) | 全文已翻译并校订（书内第 65–75 页）；含 2 幅原图、表 5-1 及中文标签对照 |
| 第 6 章 衡量与治理架构特性 | [译稿](chapters/06-measuring-and-governing/translation.md) | [笔记](chapters/06-measuring-and-governing/notes.md) | 全文已翻译并校订（书内第 77–89 页）；含 4 幅原图、5 个代码示例及中文标签对照 |
| 第 7 章 架构特性的作用范围 | [译稿](chapters/07-scope-of-architecture-characteristics/translation.md) | [笔记](chapters/07-scope-of-architecture-characteristics/notes.md) | 全文已翻译并校订（书内第 91–98 页）；含图 7-1 与中文标签对照 |
| 第 8 章 基于组件的思维 | [译稿](chapters/08-component-based-thinking/translation.md) | [笔记](chapters/08-component-based-thinking/notes.md) | 全文已翻译并校订（书内第 99–116 页）；含 11 幅原图及中文标签对照 |
| 第 9 章 基础 | [译稿](chapters/09-foundations/translation.md) | [笔记](chapters/09-foundations/notes.md) | 全文已翻译并校订（书内第 119–132 页）；含 9 幅原图及中文标签对照 |
| 第 10 章 分层架构风格 | [译稿](chapters/10-layered-architecture/translation.md) | [笔记](chapters/10-layered-architecture/notes.md) | 全文已翻译并校订（书内第 133–141 页）；含 6 幅原图与评分表中文转录 |
| 第 11 章 管道架构风格 | [译稿](chapters/11-pipeline-architecture/translation.md) | [笔记](chapters/11-pipeline-architecture/notes.md) | 全文已翻译并校订（书内第 143–148 页）；含 3 幅原图、Shell 示例和评分表中文转录 |
| 第 12 章 微内核架构风格 | [译稿](chapters/12-microkernel-architecture/translation.md) | [笔记](chapters/12-microkernel-architecture/notes.md) | 全文已翻译并校订（书内第 149–161 页）；含 8 幅原图、代码片段和评分表中文转录 |
| 第 13 章 基于服务的架构风格 | [译稿](chapters/13-service-based-architecture/translation.md) | [笔记](chapters/13-service-based-architecture/notes.md) | 全文已翻译并校订（书内第 163–177 页）；含 10 幅原图与评分表中文转录 |
| 第 14 章 事件驱动架构风格 | [译稿](chapters/14-event-driven-architecture/translation.md) | [笔记](chapters/14-event-driven-architecture/notes.md) | 全文已翻译并校订（书内第 179–209 页）；含 22 幅原图、3 张权衡表和评分表中文转录 |

[第一部分导言：基础](parts/01-foundations.md)与[第二部分导言：架构风格](parts/02-architecture-styles.md)已翻译。

## 下一处翻译

第 15 章 Space-Based Architecture Style（空间架构风格），书内第 211 页，PDF 第 231 页，从第一段开始。第 1–14 章已完成；第 15 章及以后尚未翻译。

## 原文定位

原始 PDF 保留在本工程的上级目录，不纳入版本控制：

`../Fundamentals of Software Architecture An Engineering Approach (Mark Richards, Neal Ford) (Z-Library).pdf`

书内页码与 PDF 页序分别记录；PDF 页序从 1 开始计数。

## 工作方式

1. 阅读一个完整小节，记录问题。
2. 按[翻译约定](translation-guide.md)翻译，查询并更新[术语表](glossary.md)。
3. 对照原文校订，检查否定、条件、因果、限定词与图表。
4. 在独立笔记中记录理解、项目联系与疑问。
5. 更新进度，按可独立审阅的段落或小节提交 Git。

尚未解决的跨章节问题记录在 [open-questions.md](reviews/open-questions.md)。
