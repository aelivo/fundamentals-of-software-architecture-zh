# 第14章独立复审

状态：完成本章原文逐段对照、中文全章连续通读及修改回查、22图／3表／6文本示例、相关笔记／术语与自测十题检查。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文锚点 | 译稿与结果 |
| --- | --- | --- | --- |
| 066 | 199–201 / 179–181 | 章首The event-driven、Most、A good example、An event-based；图14-1；Topology单段；Broker首段；There are four、The event broker、图14-2 | CH14-001–008逐段对照完成；图14-1／14-2页面图像核对、请求／事件对比、四要素、消息流及federated解释／主题使用限定完整；修复request范围及if needed |
| 067 | 202–204 / 182–184 | It is always、图14-3、This is；To illustrate、图14-4、The Notification；The Inventory、The Payment、The OrderFulfillment、In analyzing | CH14-009–016逐段对照；图14-3／14-4页面图像、OrderPlacement、7个后续事件与并行／先后分支均核，邮件无人订阅、库存／支付／仓储、拣货／打包／发运及1.5km接力比喻完整 |
| 068 | 205–208 / 185–188，至图14-7引导 | While、Error、The ability、表14-1；Mediator引导、Like、图14-5、In most、The event mediator、However跨页、BPEL、It is important、Given、图14-6、Notice、To illustrate | CH14-017–031均对照；页面205–208核表14-1五行优缺点与图14-5／14-6（包括BPEL／BPM、初始／处理事件分流）；恢复否定／only／would，BMP错字译注独立列出 |
| 069 | 209–212 / 189–192 | 图14-7、In keeping、Once；图14-8、Now；图14-9；Once、图14-10 | CH14-032–035逐段对照及页面209–212核图，五步概览／前三步的并发与确认、队列／命令完整；14-10源图apply-payment与正文fulfill-order不同，现有标签注释准确，保留 |
| 070 | 213–215 / 193–195 | Once、图14-11、Finally、图14-12、The mediator；Another、While、表14-2、The choice | CH14-036–043均核；页面213–215核图及五行优缺点，状态持久化、从第3步恢复、命令必须处理／事实可忽略的差别齐全 |
| 071 | 216–219 / 196–199，至委派日志 | Asynchronous两段／图14-13；This is、The difference、The main；Error Handling引导、The workflow跨页、Once／图14-14、To illustrate跨页；契约／交易篮子／Notice／堆栈／When／Applying／日志 | CH14-044–061逐段对照，图14-13／14-14页面核、四段契约／数据／堆栈／日志逐字符内容核；3,000／3,100／25／3,025毫秒、6行交易第4行SHARES、堆栈与错误委派输出均覆盖 |
| 072 | 220–222 / 200–202 | The Trade Placement／日志、The fixed／日志、图14-15、One of consequences；Preventing两段／3项列表／图14-16、Each跨221–222、Issue2、Issue3、图14-17 | CH14-062–074及三图页面均核；错误指令与两个输出示例内容一致；同账户FIFO、3个丢失点、持久化／同步发送／客户端确认／ACID／LPS按源文保留，错误与事务关系明确译注 |
| 073 | 223–226 / 203–206 | Broadcast两段／图14-18；Request-Reply两段／图14-19、There are two／6步跨页／图14-20；The other／4步跨页／图14-21、While；Choosing单段 | CH14-075–086全部对照，页面223–226核四图及数字ID124／855／856／857、CID120／122／124、NULL、reply-to／Q998；原文等待方consumer及图右侧producer异名保留提示 |
| 074 | 227–229 / 207–209 | Understanding／表14-3；Hybrid两段；Ratings引导、Event-driven／图14-22、The number、To illustrate、Event-driven、Overall、Finally | CH14-087–100全部对照；表14-3页面7优点4代价与3空白格核，图14-22页面13行核：Technical、1 to many，星数3／3／5／5／4／3／5／3／5／1／2；两量子约束、promise/future条件、竞争消费者和非确定测试问题完整 |
| 075 | 397–398 / 377–378本章十题及中文全章 | What differences；For better workflow；Does broker；Name two；Give request；Give event；What initiating；What techniques；What driving；What unsupported | APP-071–080全部核，无须改题；中文全章从标题连续读至图14-22标签末，回查PDF199、201、205–208、216–220、222、227；无新增覆盖遗漏发现 |

## 修改及理由

- PDF199 / 179、CH14-002：“用户向系统发送请求”→“发送给系统……的请求”。源文未限定请求来自用户，保留API／ESB等来源空间。
- PDF199 / 179、CH14-004：“出价不是向系统查询某件事”→“出价不是向系统发出的请求”。作者对比的是request与event，不能只排除查询而弱化其论点；保留本版建模语境，不擅自替作者重新界定请求。
- PDF201 / 181、CH14-007：“该事件发送到代理，供进一步处理”→“该处理事件异步发送……以便在需要时继续处理”。恢复再次异步发送及if needed的条件，避免暗示必有下游处理。
- PDF205 / 185、CH14-019：“无法简单重新提交”→“无法重新提交”，原文not possible不只是操作是否简单；按本版作者对broker状态管理的论述保留。
- PDF206 / 186、CH14-023：“中介者了解处理步骤”→“只了解事件处理所需的步骤，因此……”，恢复only及生成处理事件的因果。
- PDF207 / 187、CH14-028：“可能浪费数月”→“就会浪费数月时间”，原文would take months在该假设情境下是确定判断，不弱化成may。
- PDF208 / 188、CH14-030：BMP／BPM差异提示从正文移为明确译注；已核页面与图14-6，正文统一BPM仍可回查原字，不混入作者叙述。
- PDF217 / 197、CH14-047：“有一个前提”→“有一点需要注意”，caveat是提醒而非前置条件；“发表评论通常要求如此”→本例“发表评论就必须注册”，恢复would have to；“无法回到用户身边”→“无法再与用户联系”，修复get back to的机械直译。
- PDF218 / 198、CH14-051：“可能根据静态、确定性规则”→“错误可能是静态、确定性的”，避免把错误性质改成原文未说的处理规则；“若仍无法判断”→“很多时候……无法确定”，恢复many times且不暗示已修复失败才进入人工流程。
- PDF219 / 199、CH14-058：“除了记录日志，服务似乎无能为力”→“除了可能记录错误日志之外，什么也做不了”，恢复nothing can do的确定否定和possibly只修饰log的范围，维持作者在引入模式前的论证语气。
- PDF220 / 200、CH14-067：“消息会乱序”明确为“出错消息重新提交后……”，恢复对象范围；原译“维持特定上下文，此处是账户号，内的顺序”改为自然括注，补全由Trade Placement服务将账户号入队保存及后续交易FIFO的过程，不改为所有账户全局排序。
- PDF227 / 207、CH14-091：补回data pump术语及其消息实现，原译只描述传输而遗漏名称；“提高用户响应能力”恢复“提供其他架构风格不具备的用户响应能力”，保留作者比较范围，不自行弱化；后句恢复两者利用事件驱动进行程序扩展的因果。

## 原书疑点

- PDF216图14-13下方标两个25ms，正文3,025ms只计一个25ms和3,000ms，两个时延是否重叠未说明。已看原页，新增明确译注，保留原图及数值；不擅自确定应为3,050ms，列待确认。
- 图14-10的apply-payment／fulfill-order差异及BMP／BPM拼写均已核页，保留原图与明确提示。
- PDF221问题3为数据错误导致无法写入，222却直接以ACID提交解决，省略了数据错误本身的处理前提。对照同期[PostgreSQL12事务说明](https://www.postgresql.org/docs/12/tutorial-transactions.html)关于失败回滚／成功提交后持久化，译注补清事务不能自行纠正数据，正文不改作者说法。原书确认模式／LPS与端到端保证的全部实现及故障边界未独立实验，保留现有范围提示，不能据名称认证恰好一次。
- PDF225的关联ID等待方原文consumer，图14-20／14-21右侧原标producer，已核图文，保留原图与现有归属提示。图14-21左侧又列CID124，虽正文说无需CID，原图未修；现有图标签说明已经明确记录，复核后保留。
- PDF228量子段原文a request is needed…from event consumer，中文按前后文译消费者结果，含义可由下一页等待订单ID的例子支持；原词与应答流程不协调留此供回查，不猜测作者勘误。

## 附件及完成边界

- notes四条当前理解、四条适用范围、五条中介者补充、八条后半章要点逐项检查；学习解释与作者原文分离，不当作原书新增段落。
- glossary的事件驱动、代理／中介者、初始／处理事件、处理器／通道、背压、响应能力、韧性、工作流事件、关联ID、请求应答、客户端确认、LPS、竞争消费者，以及data pump的本章用法均与源文比较；data pump更完整定义留待第15章核。
- 所有小节标题、正文、表、图题／标签和文本示例均覆盖；100个译文标记包括列表、代码、表、译注，不等于原书段数，覆盖按上表内容锚点建立。
- “无人订阅消失”、单量子、BPEL／BPM产品能力、最终一致性及端到端保证等按本版语境保留并审阅现有范围提示，不作所有当前产品的普遍认证。上列原书疑点仍无作者明确勘误。
- 下一章：PDF231 / 211，CH15-001。
