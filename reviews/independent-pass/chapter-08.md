# 第8章独立复审

状态：已完成原文逐段对照、中文连续通读及回查、11图、相关笔记／术语／自测题检查。主文件`chapters/08-component-based-thinking/translation.md`。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文内容锚点 | 译稿与结果 |
| --- | --- | --- | --- |
| 035 | 119–122 / 99–102 | In Chapter3；Component Scope下Developers、Components offer、Components also、Nothing requires、Components form；Architect Role下Typically、Virtually、Generally、An architect must；Architecture Partitioning下The First Law、Consider、In Figure8-3 | CH08-001–013全部对照；图8-1–8-3页面图像及标签均核对，组件／服务／库层次与职责限定完整 |
| 036 | 123–126 / 103–106 | Organizing、图8-4、In Figure8-4、An interesting；Conway框文引入／引文／释义／Inverse；The other、One of、Architects using、The separation；图8-5、In Figure8-5、Neither；Case Study引导、图8-6、In Figure8-6、An alternative、Which、图8-7 | CH08-014–030全部对照；跨123–124框文完整连读；图8-4–8-7页面图像与标签已核，箭头／嵌套／购物车分布一致 |
| 037 | 127–130 / 107–110，至Entity trap引导与图8-9 | Domain partitioning定义及5优点1缺点；Technical partitioning定义及2优点3缺点；Many other；Developer Role两段；Component Identification引导／图8-8／This cycle；Identifying初始段；Assign／Analyze roles／Analyze characteristics／Restructure各段；Granularity、Design、Discovering、Entity trap引导 | CH08-031–050及图8-8／8-9（页面图像）均对照；五步骤循环回到roles／responsibilities，图标签完整；优缺点与条件无漏译发现 |
| 038 | 131–133 / 111–113，至BidStreamer | In Figure8-9；Naked Objects框文三段；The entity trap；Actor/Actions两段（跨页）、Event storming、Workflow两段；GGG案例两段引导、3角色各动作、Given、图8-10、In Figure8-10、VideoStreamer、BidStreamer | CH08-051–070均对照，图8-10页面已核；原书Isis等名称按本版保留，不以今天项目名称改写 |
| 039 | 134–136 / 114–116 | BidCapture、BidTracker、AuctionSession、Payment；Referring、Because、The architect；图8-11、The design、This is；Quantum Redux引导、A monolithic、Each、The ability | CH08-071–083全覆盖；页面134–135确认bidder原词与拆分前后图，新增Auctioneer capture及Bid tracker汇合关系；所有相关标签已核 |
| 040 | 395–396 / 375–376，第8章6题 | We define；What is the difference；What is the advantage；Under what circumstances；What is the entity trap；When might you choose | APP-033–038准确覆盖，workflow与actor/actions比较条件完整 |

## 修改与判断

- PDF124 / 104、CH08-023：“持久层”→“持久化层”，与前章已复核的persistence layer译名一致。
- PDF126 / 106、CH08-028：“分别覆盖通用与本地差异”→“涵盖通用与本地差异”。原文covering both，无须额外加入分别对应的暗示；图8-6显示多个组件内部各有Common与Local。
- PDF132 / 112、CH08-060：“相匹配”→“完全匹配”，恢复作者matches exactly的程度，不自行弱化作者对事件风暴与开发流程关系的判断。
- PDF134 / 114、CH08-073：移除正文中的“原文称”，作者叙述与下一行明确译注分别呈现；bidder不擅自改成auctioneer。
- MVC与分层架构、DDD工作流等历史或概念表述按作者本版语境保留；尚未据外部资料判定其技术观点。

## 通读、回查与保留事项

- 全章中文连续读至图标签末，未发现另需实质修改的衔接／指代问题；本次修改回查PDF124、126、132、134及图8-6，未增加或删去原意。
- 章节各层标题、Conway和Naked Objects框文、四组优缺点清单（5／1、2／3项）、三角色动作和六个初始组件、11幅图题／标签均已覆盖。83个译文标记用于定位，源文覆盖以上表锚点为依据。
- notes六条核心理解、七条适用范围及四项项目练习均已审阅，学习观点与原文明确区分；相关glossary条目核对见notes本次段，未发现必须更改的定义。
- 原书正文Delivery／图Deliver、正文系统动作3项／图4项、bidder结束拍卖的主体差异均经页面确认，保留现有译注或笔记。图8-11按图呈现，未自行更换箭头。
- 第10章是否充分涵盖模块化单体的交叉引用留待第10章实际检查；旧框架项目历史及RUP起源等作者断言未外部认证，译文按出版时语境保留。事件风暴的限定保留明确译注，未据今天的方法定义改写作者。
- 下一单元：第二部分引言PDF137；第9章PDF139 / 119、CH09-001。
