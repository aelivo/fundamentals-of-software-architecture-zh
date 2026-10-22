# 第12章独立复审

状态：完成本章原文逐段对照、中文连续通读及修改回查、八图含评分、四Java示例、相关笔记／术语与自测八题检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译稿与结果 |
| --- | --- | --- | --- |
| 056 | 169–172 / 149–152 | 章首The microkernel；Topology；图12-1、Core System引导与首Java；Rather than／第二Java／In this example／Depending；图12-2、The presentation | CH12-001–011全部对照；页面170–172核图12-1／12-2、两段代码及源文DevicePlugin大小写、缺括号，保留原代码及明确译注 |
| 057 | 173–176 / 153–156 | 图12-3；Plug-in引导跨页、The communication、Point-to-point、图12-4、Alternatively跨页、图12-5、Plug-in components do not、图12-6、The benefits跨页、With these、It is not | CH12-012–020全部对照；页面173–175核图12-3–12-6及名称，模板plug-in／实例plugin、图assessment_ipad4.jar与包名等均保留；运行时／编译期、同步／异步、共享库／远程及存储界限完整 |
| 058 | 177–180 / 157–160 | 图12-7；Registry两段／Java；Contracts两段／Java接口与输出类／In this contract／Notice；Examples首段跨页／Claims／Most／The claims／Another；Ratings引导／图12-8／Similar | CH12-021–040全部对照，图12-7／12-8及两段Java页面177、178、180均核；13行评分为Domain and technical、1，星数3／1／3／1／3／5／3／3／1／4／3，无漏行错星 |
| 059 | 181 / 161 | The microkernel、Testability、Modularity、Performance四段 | CH12-041–044均对照；领域／技术同构、运行时限定、税表例及WildFly移除功能例完整；most与略高于一般程度修复 |
| 060 | 397 / 377本章八题、全章中文与修改回查 | What is another；Under what situations；What tools；What would you do；Provide two；Is style；Why single quantum；What is isomorphism | APP-055–062完整准确；中文章首至全部图标签连续通读，无新增实质修改；回查PDF171、178、181和图12-2及词义证据 |

## 修改及依据

- PDF171 / 151、CH12-010：“店内信用额度”→“店内抵用余额（store credit）”。本段列支付方法，原译易误作授信贷款额度；商家给予客户、可用于本店付款的金额更符合零售语境。参考零售平台[Shopify自身的store credit说明](https://help.shopify.com/en/manual/customers/store-credit)关于余额和付款用途的术语用法，只作词义佐证，不将其当前功能／限制引入原书或推断本书指该产品。
- 图12-2中文标签“持久层”→“持久化层”，与前章已经复核的persistence layer名称一致。
- PDF178 / 158、CH12-026：“第三方……可能出现”→“定制契约通常出现在……情况下”，恢复typically及第三方开发／无法控制契约的条件。
- PDF178 / 158、CH12-031与PDF181 / 161、CH12-044：“许多”→“大多数”，恢复两处most；末段性能三星补“略高于一般水平”，保留原文评价程度，开句改为自然中文“为……评分，总是颇有意思”。

## 保留问题

- Java两例缺括号与类／实例名差异为原版页面内容，译注已核，无静默修补。
- 模板含连字符、具体示例不含，为原文差异，现有译注准确。
- 远程插件既称分布式又保留单量子、单体部署不会同样请求失败等为作者本版论述；不擅自扩充作者条件或改成现代产品保证。
- 第三段Java注册表同键覆盖、静态块引用非静态字段、第四段接口／输出类均按页面核实，保留代码及明确提示，不作为可编译实现。第三段的三条注释译稿另作中文说明，属于明确的代码说明，不误计为源文正文。
- PDF180的extensibility弱项与181的extensibility三星相矛盾，图表本身列的是Evolutionary三星和Elasticity一星，没有Extensibility行；各自保留，不猜测应改哪一词。

## 附件及完成边界

- 章首、Topology／Core／Plug-in、Registry、Contracts、Examples、Ratings全部小节及跨页段落均已核；源文覆盖按上表内容锚点建立，44个译稿标记包括译注／代码／表，不能当作原文段数。
- notes五条理解、七条校订记录、三项练习及glossary microkernel／plug-in、core system、registry、happy path、契约、extensibility／scalability相关条目已核；store credit定义新增理由见上，不作授信含义。
- 原书运行时框架、Eclipse／浏览器／WildFly及保险税表例均保留作者语境；非当前API或法规认证。源文前后矛盾尚无作者明确勘误，不猜测修正。
- 下一章：PDF183 / 163，CH13-001。
