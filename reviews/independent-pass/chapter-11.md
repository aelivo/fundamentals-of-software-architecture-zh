# 第11章独立复审

状态：完成本章原文逐段对照、中文连续通读及回查、三图含评分、代码、自测六题与相关笔记／术语检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译文与结果 |
| --- | --- | --- | --- |
| 052 | 163–166 / 143–146 | 章首One of、Developers；Topology、图11-1、The pipes；Pipes单段；Filters引导／四类定义／The unidirectional跨页／六行Shell／Even；Example两段、图11-2、Notice与This example；Ratings引导及The pipeline | CH11-001–023逐段对照完成（含译注与代码）；图11-1／11-2及Shell页面图像均已核，单向／点对点、可选转换／输出、Duration与Uptime分支及MongoDB流向完整 |
| 053 | 167–168 / 147–148 | 图11-3；Overall cost、Deployability、Like、Elasticity、Pipeline architectures | CH11-024–031全部对照；评分表页面13行逐项确认：Technical、1，星数2／1／3／1／3／5／2／3／1／5／3，与中文转录相符 |
| 054 | 396 / 376，本章六题 | Can pipes；Name the four；Can a filter；Is style technically；In what way；Provide two | APP-049–054均已对照，双向、多个输出管道及模块化问题均完整，无须修改 |
| 055 | 全章中文与本次修改原文位置 | 中文章首至标签末连续通读；回查PDF163、166、168 | 完成，无新增实质修改；正文与学习整理分明 |

## 发现与修改

- PDF163 / 143、CH11-001：“拆分为独立部分……自然出现”→“决定把功能拆分为不同部分……随之出现”。discrete不直接断言各部分独立，恢复as soon as decided的叙述。
- PDF166 / 146、CH11-021：“可扩展性”→“可扩充性”。原文extensibility，例子是添加新指标的功能；与第4章定义及glossary区分，不能混为本章末scalability的负载扩展能力。
- PDF168 / 148、CH11-029：“用户界面、后端处理和数据库都部署在同一个单体中”→“采用单体用户界面、后端处理和单体数据库”。原文不额外断言三者在同一物理部署单元，避免与此前外部数据库拓扑混淆。
- CH11-031译注“两层面”改“两处”，不在没有证据时替作者解释模块化前后不一致。

## 原书问题与附件

- tester类比reduce确为PDF164原文，已有译注标明非严格定义；未替换作者类比。
- PDF165图为Service Info Capture，166后文为Service Metrics Capture；两名经图／文核实，保留原差异提示。
- PDF167肯定模块化、168又说缺乏架构模块化；保留两句与译注，未猜测作者想说哪一种模块化。
- Shell六行、反斜杠n、${1}q与页面一致；仅读取核对，不执行原书程序。Unix故事按作者叙述保留，未外部核实。
- notes四条核心理解、五条校订说明、两项练习已比较；glossary pipeline、pipe／filter、四类过滤器、telemetry及extensibility／scalability均与本章语境相符。

## 完成边界

标题、各节正文、四类过滤器定义、Shell、三图题／标签／评分、自测题均覆盖；31个标记包括代码／译注／表等，仅作译稿定位，不作为原文段数。源文问题仍保留，未找到作者明确勘误。下一章PDF169 / 149、CH12-001。
