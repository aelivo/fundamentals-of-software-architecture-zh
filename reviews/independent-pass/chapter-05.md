# 第 5 章独立复审

状态：全章原文逐段对照、中文连续通读、实质修改回查、两幅图、表5-1、学习笔记、相关术语与本章五题完成。日期：2026-10-22。文件：`chapters/05-identifying-architectural-characteristics/translation.md`、同目录notes、相关glossary与本章附录题。

## 源文覆盖

| 批次 | PDF / 书内页 | 原文结构与内容 | 译稿定位 | 结果 |
| --- | --- | --- | --- | --- |
| 023 | 85–89 / 65–69，至Kata框文结束 | Identifying；An architect；Domain Concerns两段（跨85–86）；Vasa框文；Many architects；Most architecture；表5-1；One important含基金定价完整例；Requirements全段（跨87–88）；Kata框文所有段落、Brooks引文、四类字段（跨88–89） | CH05-001–021，表5-1 | 全覆盖；至少三种来源、最重要三项无需排序、85%、1000人／10小时／末10分钟、少于六次、45分钟及表五行映射均保留；PDF86–87图像核实框文及表格 |
| 024 | 89–92 / 69–72，至需求7分析 | Case Study引导；Description/Users/6项Requirements/3项Additional context；Given；Explicit引导；用户规模、弹性对比及两图；酒店与演唱会例；三明治流量；9项分析中的1–7项（第1项跨91–92） | CH05-022–040，图5-1–5-2 | 全覆盖；PDF90–91核图坐标和曲线、图题；必须集成与后文必须提供可选集成差异按原书保留，不擅自统一；native web applications保留译注 |
| 025 | 93–95 / 73–75 | 需求8/9；The third；We also；Implicit三段；The last；Mark引文；Design Versus Architecture框文三段；An architect could跨94–95；Architects must | CH05-041–054 | 全覆盖；国际化、易用性、性能与规模基线、支付条件、可定制性、模板方法、团队协作及删减特性优先级均保留；源文两种正确／错误答案表述不改写 |
| 026 | 394 / 374，第5章五题 | 精简特性理由、来源判断、上市时间映射、scalability/elasticity、收购与客户增长 | APP-021–025 | 逐题对照，most／真伪问法、例中交付新功能与修复缺陷、收购规模限定均完整，无改动 |

## 典型处理

| 原文位置 | 原译 → 修改后 | 原因 |
| --- | --- | --- |
| PDF86 / 66，CH05-005译注 | 仅说未核验历史 → 明确指出打捞年份原书有误，正文保留 | 原书写early 20th century，博物馆资料为1961-04-24；不再把已查证的错误只列作未验证 |
| PDF90 / 70，CH05-030 | “可能还需要弹性” → “很可能还需要弹性” | probably比仅表示可能更强，恢复作者对突发流量需求的判断程度 |
| PDF93 / 73，CH05-041 | “通常不必用特殊结构” → “应该无须专门的结构支持” | shouldn’t require是判断／预期，不是typically的频率陈述；保留紧接的certainly drive设计决策 |

## 原书问题与证据

- PDF86框文确写early 20th century；[瓦萨博物馆 The Excavation](https://www.vasamuseet.se/en/explore/vasa-history/excavation)明确船于1961-04-24重见天日。本次只对这一明确年代差异定稿，不猜测修正国王要求、火炮尺寸和鸣炮等其他历史细节。
- PDF92原文native web applications确实如此；保留现译“原生Web应用”及现有译注，不静默改成“原生移动应用”。
- PDF94先说没有正确答案、只有不正确答案，紧接Mark引文却说没有错误答案、只有昂贵答案；两种说法确实同时存在。现译各自保留，不为消除表面张力改成“没有唯一正确答案”。
- 图5-1图题涉及性能，但纵轴确为Users而非性能值；文末说明为用户规模随时间变化，正确。没有擅自给图加性能单位。
- 弹性在“显式特性”小节中仍由未明写的领域知识推导；作者安排保留。案例6项需求＋3项补充背景随后统一编号1–9；译稿无漏项或重复。

## 通读、回查与附件

- 对照后连续通读本章中文全文（两段完整读取，含图题、表、框文、两组列表与所有译注），没有新增实质改写；随后回查PDF86页面、90英文与93英文及博物馆资料，确认三处修订未替换作者观点。
- glossary的architecture kata、customizability、internationalization、sacrificial architecture和Ivory Tower Architect按本章语境复核；既有译法可以保留。可扩展性／弹性、可用性／可靠性与第1–4章已核范围一致，完整跨章检查仍待全书完成。
- notes六条理解、练习与原文疑点清单已复核；修正过时的“未核验打捞年代”状态，没有把未查的其他历史细节一并标记证实。
- 五行表映射、六项初始需求、三项背景、九项逐条分析、两幅图及文末坐标标签完整；本章没有独立数学公式或代码清单。

## 保留事项与下一处

瓦萨号其他历史细节未逐项定论；native web applications、两种正确／错误说法、图注与轴的差异保留并记录。它们不阻止忠实译文定稿，但不能据译文证明源文事实。下一处第6章PDF97 / 77，CH06-001。
