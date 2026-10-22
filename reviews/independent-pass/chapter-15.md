# 第15章独立复审

状态：完成原文逐段对照、中文连续通读与修改回查、十五图／公式／四数值表／比较表／评分及Java与日志、相关笔记／术语／自测十题检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译稿与结果 |
| --- | --- | --- | --- |
| 076 | 231–234 / 211–214，至Messaging grid末 | Most、In any、图15-1、The space-based、General首段；There are several／图15-2；Processing Unit／图15-3；Virtualized、Messaging | CH15-001–020全部对照，图15-1–15-3页面核；瓶颈递移、三角拓扑、near-infinite、复制内存网格、五类组件、单元／四中间件及负载均衡条件完整 |
| 077 | 235–238 / 215–218，至Processing grid首段末 | 图15-4、Data grid引导／图15-5、Data is／Java／All；Data replication、Each／单实例日志、When another／两实例日志、When third／跨页三实例日志、Notice、When down／两实例日志；Processing grid | CH15-021–042均对照，页面235–236核图15-4／15-5与Java；IP端口／UUID／this、size与ver的1→2→3→2及最后ver4日志完整；启动缓存来源至少一个存活实例的条件保留。图15-6仍待核 |
| 078 | 239–242 / 219–222，至Data Readers引导末 | 图15-6、Deployment、Data Pumps引导、Data pumps／图15-7／In most／Data pumps usually；Writers两段／图15-8、Alternatively／图15-9；Readers引导 | CH15-043–063逐段对照，页面239–242核图15-6–15-9及领域／专用写入器、4个Profile／Wishlist／Wallet／Preferences流程；三种数据读取触发条件完整，未发现必须修改之处 |
| 079 | 243–246 / 223–226，含Cloud引导 | In the event／图15-10／Like／The data跨页／A data abstraction；Data Collisions引导／To illustrate／6步／There are several／公式／where／This formula／4张数值表及各解释／Under normal；Cloud引导 | CH15-064–090均对照；页面243–246核图、公式（RL为乘数）、六步500→490／495→485、4表各7行和缺连接词原页；独立重算14.4、0.144、5.76、72次/小时与0.02%、0.0002%、0.008%、0.1%，旧译注数值准确，保留原表舍入 |
| 080 | 247–250 / 227–230，至Near-Cache首段 | A powerful／图15-11；Replicated首段、With跨页／图15-12、Replicated、While、Distributed跨页／图15-13、When size／表15-1／When choosing；Near-cache首段 | CH15-091–112全部对照；页面247–250核3图及5行比较表，100MB／500MB、专有同步／异步协议、混合使用、MRU／MFU／RR按本版完整保留 |
| 081 | 251–254 / 231–234 | 图15-14、While；Implementation首段、Concert两段、Online两段；Ratings引导／图15-15、Notice、While、Testing、Cost、It is difficult、The number | CH15-113–137及所有图标签均核；图15-14／15-15页面核，13行Domain and technical、1 to many，星数3／5／3／3／3／2／5／4／5／1／1；10,000／数百万／提前预热条件、量子同步关系完整 |
| 082 | 398 / 378本章十题及全章中文 | Where name；What primary；Name four；What messaging；What writer；Under what reader；Does small cache；What difference cache；List three；Why testability | APP-081–090全部核，无须修改；中文连续通读至15行图标签表末，回查PDF233、245、248、254本次四处修改，无新增内容遗漏发现 |

## 修改与判断

- PDF233 / 213、CH15-010：“执行数据泵所传递更新的数据写入器”→“将数据泵传来的更新写入数据库的数据写入器”，明确中文动作及宾语，不改数据泵与写入器职责。
- PDF245 / 225、CH15-080：“100毫秒……也是我们……经常使用的数值”→“实际复制延迟（这是我们经常用来估算……的数值）……100毫秒可作为……规划估值”。a value we frequently use修饰actual replication latency，不将作者常用实际延迟误译为常用100ms假设值；保留无实测值时使用规划估值的条件。
- 中文通读PDF248 / 228、CH15-100，将悬空的“由于每个处理单元使用的内存量”改为“每个处理单元都要为缓存占用内存，因此……”，明确因果而保留100MB及might限定；PDF254 / 234、CH15-135“高资源利用量”改“大量……资源”，在成本语境指资源消耗，不混为利用效率。
- 其余本批内容未发现必须修改的语义问题，保留已有准确表达。原书“近乎无限”、图示同步／实际异步、命名缓存成员列表及始终同步等表述均按源文保留，需结合后文限制审阅附件，不以今天API行为改写。

## 原书疑点与数值核实

- PDF245原文update rate in milliseconds与表20 updates/second单位表述不充分；统一时间单位后可复现四表。采用UR20/s、RL0.1s等，计算N×20²/S×RL×3600；第二例0.144/h表列0.1，第三例5.76/h表列5.8／正文约6；百分比以72,000/h为分母均相符。只是重现作者算例，不证明该概率模型适用所有更新分布／并发行为。
- PDF246页面确实缺cloud-based environments与on-premises间的连接词；现有译注按后文两类环境理解准确，未静默补作无疑原文。
- “吞吐量超过10,000并发用户”、100MB／500MB范围及集中式distributed cache、MRU／MFU保留集合与淘汰名称、近乎无限扩展等均按源文和既有范围说明保留，未以当前缓存产品观点改写。公式概率假设／当今实现保障不作外部认证。

## 附件及完成边界

- notes八条理解、公式复算表及解释、五项项目练习和七条适用范围逐项审阅；明确不属原书正文。glossary空间架构、元组空间、处理单元、中间件四组件、数据泵／反向泵、读写器、数据抽象层、两类缓存、冲突、复制延迟及近端缓存定义与本章语境相符，无须另改术语。
- 新增只读脚本check_image_sources.py：核工程PNG像素与PDF对应图号页的嵌入图，第15章15／15一致；只核图像来源与所在页，不证明图意或翻译正确，内容另经本章页面审阅。
- 本章各节正文、全部列表／代码／图／表、译注、自测均已覆盖，141个译文标记含标题、图题、图像、分隔符和译者表，不能当作原文段数。覆盖按上表源文内容锚点建立。
- 下一章PDF255 / 235，CH16-001。
