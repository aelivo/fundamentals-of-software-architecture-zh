# 第一部分导言与第 2 章独立复审

状态：第一部分导言及本章原文对照、中文连续通读、实质修改回查、九幅图与标签、表2-1、笔记、相关术语及附录本章四题已完成。日期：2026-10-22。文件：`parts/01-foundations.md`、`chapters/02-architectural-thinking/translation.md` 及同目录笔记；附录本章题。

## 源文覆盖

| 批次 | PDF / 书内页 | 源文定位与内容 | 译稿定位 | 结果 |
| --- | --- | --- | --- | --- |
| 007 | 41（无印码） | PART I / Foundations；To understand 全段 | P01-001 | 标题、组件／模块化／耦合／共变性及 must 完整；中文单独通读，保留现译。42为空白页 |
| 008 | 43–45 / 23–25（至 Architecture Versus Design 结束） | An architect sees；Architectural thinking；In this chapter；The difference；Consider（跨43–44）；There are several；To make；Unlike；图 2-1、2-2 | CH02-001–008，图题及标签 | 全部对照，虚拟与实体屏障、单向交接／双向协作、同一虚拟团队及同步关系完整；PDF 44–45 页面核对图中文字与箭头 |
| 009 | 45–48 / 25–28 | The scope；As shown；Stuff you know（三类知识在同段）；A developer’s；In Figure 2-4；However；As an architect；图 2-3–2-5 | CH02-009–015 | 全部对照，金字塔层级、技术广深、五种候选方案、一两年期限一致；PDF 46–48 图像核对范围箭头、标签与图题 |
| 010 | 49–52 / 29–32 | Our knowledge；Architects should；Frozen Caveman 框文两段；Analyzing 两段引导及Mark/Neal引文；For example；The Bid Producer；The two messaging；The clear advantage；With this analysis及Hickey引文；图2-6–2-9 | CH02-016–029，全部图题与标签 | 全覆盖；PDF49、51、52核对图像。三个接收服务、每场拍卖所有出价历史、新增队列／订阅的修改成本与耦合关系相符；恢复箭囊比喻 |
| 011 | 53–56 / 33–36 | Thinking architecturally；In addition；Another disadvantage；Given；表2-1；The point；Understanding 全段；Balancing 下全部11段（CH02-039跨54–55、045跨55–56连读） | CH02-030–047，表2-1，现有两条译注 | 全覆盖；PDF53图像核对表的2项优点／3项缺点及空格行；保持条件、1–3迭代、两项POC理由及可选实践的完整性；原书问题另记 |
| 012 | 393 / 373，第2章自测 | 传统架构与开发、三层知识、技术广深、保持动手实践，共4题 | APP-005–008 | 逐题对照，原编号与提问内容相符，无需修改 |

## 发现与修改

| 原文位置 | 原译 → 修改后 | 理由 |
| --- | --- | --- |
| PDF44 / 24，CH02-006 | “常常无法发挥作用／往往无法实现最初的目标” → “很少能发挥作用／很少能实现最初的目标” | 两个 rarely 均表示很少成功，恢复原文的频率和强调程度；不是泛指有时失败 |
| PDF49 / 29，CH02-017 | “为解决问题储备更多可选手段” → “拥有更大的‘箭囊’，解决问题时有更多的‘箭’可选” | 原译意思基本正确，但删掉了作者箭囊／取箭的比喻；恢复教学语气，未增添技术论断 |

### 源文问题与保留

- PDF53 / 33 明确写主题的开放访问、恶意消费者导致队列丢失通知、主题同构契约及消息数监控限制。现译准确保留，已有译注将其与具体实现／配置的保证区分；原书随后明确说 monitoring/auto-scaling 权衡依技术而定，故不把技术限定擅自扩大为作者对所有前述主张的自我修正。
- PDF55–56 / 35–36 先说 four basic ways，随后依次叙述POC、债务／架构故事、缺陷、自动化、代码评审。原文数量与叙述存在张力；保留“四种”与现有译注，不静默改成五种。
- 表2-1第三条缺点没有配对的优点，现有空单元格正确；不把同一行误解为独立对应关系。

## 通读、附件及回查

- 脱离英文连续读取本章中文（分两段完整输出，无截断），没有新增实质改写；随后重读PDF44、49，核实rarely与箭囊比喻。
- 笔记的六项核心理解与正文相符，项目练习与作者观点分开；两条源文问题说明及表格空单元格说明经原文重新核实，没有沿用旧完成状态。
- glossary中 architectural thinking、technical breadth/depth、business drivers、extensibility、topic/queue、contract、programmatic load balancing、bottleneck trap、POC、两种story和code review逐项按本章语境验证，现译可保留。“可扩充性”区分功能增加与scalability负载扩展，符合本例；不强制将所有语境中的同一词译作同一词。
- PDF55–56页面再次核实“四种”与后续列举确为原书写法。九幅图均查看原页图像及标签，表2-1按实际列归属核对。本章没有独立公式或代码清单。

## 尚未完成

本章没有未定稿的翻译问题；消息产品的一般能力不能由该例证明，源文问题保留。跨章术语、案例和译注一致性留至全书逐段完成后进行。下一处为第3章PDF57 / 37，首段First, we want to untangle，CH03-001。
