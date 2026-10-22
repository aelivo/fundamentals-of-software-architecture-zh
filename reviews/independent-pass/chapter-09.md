# 第二部分引言及第9章独立复审

状态：第二部分引言及第9章完成原文逐段对照、中文连续通读及修改回查；本章图、脚注、引文、清单、笔记／术语／自测题完成检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译稿及结果 |
| --- | --- | --- | --- |
| 042 | 137部分引言；139–142 / 119–122 | 引言The difference、Understanding两段；第9章Architecture styles、Each name、Fundamental Patterns；Big Ball定义／引文／In modern／In general／Unfortunately／The client及脚注；Unitary两段；Client/Server两段及Desktop、Browser、Three-tier三段 | P02-001–002及CH09-001–019全部核对；图9-1页面141已核，原引文、年代、拓扑和两层／三层作者分类保留。部分引言中文连续通读无修改；不将tier与layer混同 |
| 043 | 143–146 / 123–126，至印记耦合解法前 | Three-tier框文两段；Monolithic引导和3／5项风格清单；Distributed、Fallacy1全文；Fallacy2三段；Fallacy3三段（跨146–147） | CH09-020–032全部对照，143–146页面均已核（Java原词、清单、图9-2–9-4、关系式、单位）；原书Java错误明确译注，恢复most／分布式能力措辞 |
| 044 | 147–148 / 127–128 | 印记耦合5项解法、Regardless；Fallacy4单段；Fallacy5三段 | CH09-033–038已对照，图9-5／9-6图像待核；most／tend to／magnitudes恢复原强度 |
| 045 | 149–152 / 129–132；147–151图像 | Fallacy6单段、Fallacy7两段、Fallacy8两段；Other Distributed引导；Logging两段（跨页）、Transactions三段、Contract单段 | CH09-039–050完成对照；图9-5–9-9页面及标签均已核，未发现缺图或标签遗漏 |
| 046 | 396 / 376本章四题及全章中文 | List／Name／What is／What are四题；章首至图标签末连续通读 | APP-039–042完整且准确；附录题名Architecture Styles不同于正文Foundations，页面确认，保留译注；通读后无需再改实质内容，修改回查PDF143–147、149、151–152 |

## 发现与修改

- PDF143 / 123、CH09-020：原译只写序列化说法“存在疑点”；页面确认原书确实写Every Object。对照Java SE8的[Object声明](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)和[Serializable定义](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)，现译注明确Object未实现该接口，类须直接或继承实现该接口才具备其标识的性质，正文保留作者断言。Oracle2000年文章亦明说Object不实现Serializable，但采用API作为直接证据；使用程度等历史断言不作外部认证。
- PDF144 / 124、CH09-025：“虽然可以比……强大”→“虽然比……强大”。原文being much more powerful是作者此处的判断，不自行弱化成能力可能性；不据此宣称一切实际系统都如此。
- PDF145 / 125、CH09-027：“许多架构师”→“大多数架构师”，恢复most。
- PDF146 / 126、CH09-031–034：页面确认500kb、1Gb、200bytes、400kb确为源文。现有笼统单位译注补入200字节×2,000/秒＝400kB/s＝3.2Mb/s的十进制校算；保留正文单位，不猜作者前两项b的本意。
- PDF147 / 127、CH09-035：“许多……因而忘记”→“大多数……因而往往忘记”；“大幅”→“按数量级”，分别恢复most、tend to及magnitudes。
- PDF149 / 129、CH09-039：删除“不需要”前的“通常”，原文此处未加频率限定；保留作者判断，不自行缓和。
- PDF151 / 131、CH09-043：“不可能测试所有”→“并非所有……都经过了充分测试”。原文是未充分测试的事实陈述，不是宣称无法测试；恢复由此造成丢包的因果关系。
- PDF151–152 / 131–132、CH09-045的“要根因分析”改为“要通过根因分析查明”，修复中文搭配；CH09-048“独立部署单元”改“不同部署单元”，separate不额外推出independently deployable。
- PDF152 / 132、glossary contract由“服务所接受的数据与约定”补为“客户端与服务共同约定的行为和数据”，避免漏掉本章明确定义的行为及双方关系，后续相关章节须以同样定义检查。

## 附件及保留问题

- 正文标题、三层架构框文、大泥球长引文及XRay脚注、九图与所有列表完整；按源文锚点核覆盖，50个标记只是译文定位。
- notes六条理解、五条范围说明和四项练习均已核，学习解释与原文区分。glossary相关的unitary／client-server／fallacies／circuit-breaker／tail-latency／stamp-coupling／CDC／eventual-consistency／saga／event-sourcing与本版上下文相符；contract补全后与本章定义相符。
- 部分引言区分style和pattern，而章首允许两名混称，是原书叙述层次，不擅自统一改掉。浏览器架构仍称two-tier、Java／.NET及三层历史、序列化使用率、网络设备互操作、Saga／BASE等宽泛判断按作者语境保留，现有范围译注已审阅，不作普遍技术认证。
- 单位b原意、作者序列化／Saga措辞的确切勘误仍未确定，见open-questions；对照完成不等于不存在原书错误。
- 下一章：第10章PDF153 / 133，CH10-001。
