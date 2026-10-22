# 第 1 章独立复审

状态：本章独立原文对照、中文连续通读、实质修改回查、7幅图与中文标签、学习笔记及本章4道自测题均已完成。日期：2026-10-22。译稿 `chapters/01-introduction/translation.md`；学习笔记同目录 `notes.md`；自测题在附录第 1 章部分。

## 源文覆盖

| 批次 | PDF / 书内页 | 独立核对的源文内容 | 译稿定位 | 结果 |
| --- | --- | --- | --- | --- |
| 001 | 21–24 / 1–4 | The job；First（含 Fowler 引文及 Ralph Johnson 归属）；When pressed；Second；Third；Fourth；Why a book；When studying；Defining Software Architecture 首段及 Figure 1-2 引导；图 1-1、1-2 及图题 | CH01-001–011，图 1-1–1-2，文末相应标签 | 全覆盖。50/30/至少50份许可数、四个定义维度、历史限定和交叉引用一致；未发现需改的正文问题。PDF 22、24 图像核对，图 1-1 所有分支及标签均有中文对照；代码缩略图是示意背景，不需逐字转录 |
| 002 | 25–28 / 5–8 | The structure；Architecture characteristics；The next factor；If a particular；The last factor；Expectations 标题下两段及八项列表；图 1-3–1-6 | CH01-012–019，图题及相应标签 | 全覆盖。PDF 25–28 页面图像核对架构结构、12项特性、层间访问限制、异步通信原则与工作流归属；正文与图 1-5 的数据库／持久化层差异确实存在，保留译注 |
| 003 | 29–33 / 9–13（末页至 Expectations 结束） | The first key；八项期望的各引导句及其全部解释段，CRM 段跨 32–33 连读；The main point 总结 | CH01-020–046 | 全覆盖。修正 must 的强制程度；保留三年以上、十种缓存产品、领导力至少一半等限定；第 6、19、23、24 章引用相符 |
| 004 | 33–37 / 13–17（末页至 Engineering Practices 结束） | The scope；Pets.com 框内三段；The following sections；Engineering Practices 两段；XP 框内三段（34–35 连读）；Focusing；Rumsfeld 引文；Unknown unknowns；Mark 引文；Thus；Often；The evolution；As any experience；Building Evolutionary Architectures 两段；We won’t go；图 1-7 | CH01-047–067，图 1-7 与标签 | 全覆盖。1990年代初／1996年3月、流程与实践区别、旅行商与路径长度、适应度函数的客观评估含义一致。PDF 34–36 页面核对框文边界及图 1-7 的7项标签 |
| 005 | 37–40 / 17–20（从 Operations） | The most obvious；However（跨37–38）；The builders；Process 三段；Data 两段；Laws 引导、两条定律、推论及各自解释段（末段跨39–40）；Throughout | CH01-068–083 | 全覆盖；否定、条件、全部引用及定律归属一致；作者概念无静默改写 |
| 006 | 393 / 373，第1章自测 | 四个维度、决策与原则区别、八项期望、第一定律，共4题 | APP-001–004 | 与源文逐题核对，编号及问题内容完整，无改动 |

## 修改、原书问题与未决

| 原文位置 | 原译 → 修改后 | 理由 |
| --- | --- | --- |
| PDF 31 / 11，This expectation does not mean，CH01-035 | “至少应熟悉多种技术” → “至少必须熟悉多种技术” | 原文 must at least，恢复强制程度；后句 should 仍译“应当” |
| PDF 33 / 13，The scope，CH01-047 | “许多公司” → “大多数公司” | 原文 Most companies，恢复多数范围；批次004完整核对并回查 |

首批未发现需要修改的内容。按原文保留作者关于微服务变更成本和历史软件价格的论断，不据当前技术观点改写。reactive-based 框架分类按本版原文保留。Pets.com 案例保持作者叙述，未将其当作独立查实的公司历史。

## 术语与附件独立核实

- glossary 中本章的架构特性、决策、原则、例外许可、架构生命力、结构退化、适应度函数、应用孤岛、弹性伸缩和权衡等条目与本章定义／语境相符，保留；架构量子目前仅被引入，其完整定义留至第7章核实。不能因已出现于本章，就宣布术语表全部验证完成。
- PDF 31 / 11 的四个金融例词重新核验含义：ADX 是趋势强度指标，见 [Fidelity 术语表](https://www.fidelity.com/webcontent/ap010098-etf-content/19.11.0/help/research/learn_er_glossary_1.shtml)；aleatory 指履约依赖不确定事件，保留“射幸合同”，见 [Cornell LII](https://www.law.cornell.edu/wex/aleatory)；nonpriority 保留“非优先债务”，未擅自等同次级债，参见 [美国法院 Schedule E/F 说明](https://www.ganb.uscourts.gov/content/opm/schedule-ef)。仅用于术语辨义，不将现行法律或市场观点增入译文。
- rates rally 保留“利率市场走强”。本次独立依据 [CME 的 TBA/Treasury 说明](https://www.cmegroup.com/articles/2024/spreading-treasury-and-tba-futures-to-manage-the-mortgage-basis.html) AI-Durations 小节：将这种行情与较低的债券等价收益率相联系。原书未展开定义，故正文不擅自增添长篇解释。旧 BlackRock 链接本次直接打开跳转错误页，不把其搜索摘要当作唯一核验证据；更新 glossary 指向本次报告，旧报告保留。
- notes 的核心理解、项目联系与疑问已重新阅读，且与作者正文分开；没有把学习练习当作原文。删除其过时的“尚未独立复审”状态，另记本次结论。
- 本章没有公式、独立代码清单或表格；两段框文及引文均已覆盖。7个图像文件存在，图题和文末对照的编号一致。

## 中文连续通读与回查

在英文对照后，连续读取本章中文全文（含图题及文末标签），检查衔接、指代和论证顺序；工具输出截断的中段另行完整补读。没有在通读阶段产生新的实质改写。两处正文修改再次回查 PDF 31、33 的 must at least / Most companies，未增删论点。

## 尚未完成

本章无悬而未决的翻译修改；原书分类和案例历史的真实性没有因此得到独立证明。全书术语、案例、译注和交叉引用一致性检查仍须待其余章节审完后进行。本章既有金融词译法保留不代表继承旧复核结论。
