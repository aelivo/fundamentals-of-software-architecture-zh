# 第13章独立复审

状态：完成原文逐段对照、中文连续通读与回查、十图及评分、相关笔记／术语与自测八题检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译稿与结果 |
| --- | --- | --- | --- |
| 061 | 183–186 / 163–166 | Service-based引导；Topology两段、图13-1、In most、Services are、One important；Topology Variants引导／图13-2、Similarly／图13-3 | CH13-001–008均对照；页面184–186核三图、4–12／平均7、单体库与各自库、UI三种组合、容器非必要及通信条件 |
| 062 | 187–191 / 167–171，至数据库划分末 | Finally／图13-4；Service Design引导、图13-5、Regardless、Because跨页、To illustrate、Domain services；Database引导、Within／图13-6、One way跨190–191／图13-7、Notice、建议框文 | CH13-009–019全部对照；图13-4–13-7页面图像及标签均核，两个完整跨页论证、ACID与BASE、订单／支付／库存条件、单库与分领域实体库、公共表协调均覆盖 |
| 063 | 192–195 / 172–175，至量子图末 | Example三段、图13-8、This example；Ratings引导、图13-9、Service-based跨页、Being、图13-10 | CH13-020–029全部对照；页面193–195核图13-8–13-10、七服务与三UI、两库两量子、横向分隔线；13行评分为Domain、1 to many，星数4／2／3／4／4／4／3／4／3／3／4，与转录相符 |
| 064 | 196–197 / 176–177 | Although、Fault tolerance、Scalability、Simplicity、Service-based；When to Use四段（The flexibility、Service-based、Maintaining、Lastly） | CH13-030–039均对照；四星取舍、扩展／弹性、单实例条件、50km/h法拉利比喻、DDD／ACID及两次both必要性完整；强制程度恢复 |
| 065 | 397 / 377本章八题及中文通读／回查 | How many；Do you have to；Under what circumstances；What technique；Do services require；Which characteristics；Why elasticity；How increase quanta | APP-063–070均核；第3题might want不强化为需要；中文章首至图标签末连续通读后，回查PDF187、190、196–197及397，无新增覆盖缺漏发现 |

## 发现与修改

- PDF187 / 167及图13-5：持久层→持久化层，与前章已复核的Persistence Layer译名一致，图英文Layered design等标签保留。
- PDF196 / 176、CH13-033：“较易实现且成本有效”→“最容易实现且成本效益较高”；“相关评分也可能改善”→“成本和复杂性越高，这些评分就越好”。恢复one of the easiest及the higher…better的作者判断，不自行添加可能性缓和论断。
- PDF197 / 177、CH13-035：“其他分布式风格当然更强大”→“当然有其他分布式架构风格强大得多”。原文存在其他强大得多的风格，不泛指所有其他风格，并恢复much more程度。
- PDF197 / 177、CH13-038：原译将both orchestration and choreography are required／necessary两处降为“需要协调／这两类方式用于”；恢复“编排与协同都是必需的”及末尾再次必要性。原书论述的适用范围通过明确译注说明，不在正文静默删改作者强调。
- PDF397 / 377、APP-065：“什么情况下可能需要拆分数据库”→“在什么情况下，你会考虑拆分数据库”，原文might want是选择意愿，不是需求必要性。
- 中文通读CH13-016“最不有效”→“效果最差”，回查PDF190的least effective，改善搭配而不将effectiveness改为执行效率。

## 原书与附件问题

- PDF192称vertical line，193／195图实际横向隔离线，已核图保留现有译注。
- 两次both必要性为作者原文，修复正文之后译注也明确两处原词；不据此认证每个工作流必须同时实施两种机制。
- 共享库变更传播、BASE／ACID、单量子与共享UI／DB、可用性／容错等为本版语境的架构论断，现有学习笔记说明实施边界已比较；不以当前产品或个人技术偏好改写。
- notes六条核心理解、七条适用范围及四项项目练习已比较，清楚区分学习内容。glossary service-based／domain service／API facade／orchestration-choreography及量子／契约／ACID相关定义与本章相符，未发现必须修改的术语。

## 完成边界

全章标题、正文、建议框文、表、图题／标签、译注、自测均已覆盖。39个译文标记包含译注／表，只作定位，源文覆盖以上表锚点为依据。原书架构论断和勘误疑点未作绝对认证，下一章PDF199 / 179、CH14-001。
