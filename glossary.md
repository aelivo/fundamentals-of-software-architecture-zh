# 术语表

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| software architecture | 软件架构 | 全书统一 |
| software architect | 软件架构师 | 首次出现保留英文 |
| career path | 职业发展路径 | 第 1 章第一段 |
| nurse practitioner | 高级执业护士 | 区别于泛指的护士 |
| finance manager | 财务经理 | 第 1 章第一段 |
| architecture characteristics | 架构特性 | “-ilities”泛指各类质量特性；按原文语境处理 |
| architecture decisions | 架构决策 | 规定构建系统时应遵循的规则 |
| design principles | 设计原则 | 指导方针，与强制规则区分 |
| architecture style | 架构风格 | 如分层、微服务、微内核 |
| variance | 例外许可 | 对架构规则的正式偏离许可 |
| architecture review board (ARB) | 架构评审委员会 | 首次出现附缩写 |
| architecture vitality | 架构生命力 | 架构随业务和技术变化而保持适用的程度 |
| structural decay | 结构退化 | 代码或设计变更损害所需架构特性 |
| fitness function | 适应度函数 | 第 1 章以演化计算为背景引入 |
| architectural fitness function | 架构适应度函数 | 客观验证架构特性是否得到保持 |
| evolutionary architecture | 演进式架构 | 保持术语一致 |
| architectural quantum | 架构量子 | 本章仅引入，第 7 章再展开 |
| engineering practices | 工程实践 | 与团队组织和互动的流程区分 |
| continuous integration | 持续集成 | 可保留缩写 CI |
| continuous delivery | 持续交付 | 书名保持英文对应 |
| cyclomatic complexity | 圈复杂度 | 第 1 章策略模式例子 |
| application silo | 应用孤岛 | 本章指数据库只能由所属应用访问 |
| elastic scale | 弹性伸缩 | 根据需要增减资源实例 |
| scalability | 可扩展性 | 与弹性区分 |
| availability | 可用性 | 与可靠性区分 |
| reliability | 可靠性 | 与可用性区分 |
| accidental complexity | 偶然复杂性 | 第 1 章运维讨论 |
| Big Design Up Front | 前期大设计 | 首次出现保留英文 |
| Strangler Pattern | 绞杀者模式 | 渐进迁移架构的模式 |
| feature toggles | 特性开关 | 保留原文链接 |
| trade-off | 权衡 | 全书统一；必要时以“取舍”表达动作 |
| architecture decision record (ADR) | 架构决策记录 | 本章结尾指向第 19 章 |
| architectural thinking | 架构思维 | 以架构视角分析问题，不仅是思考架构本身 |
| technical breadth | 技术广度 | 所了解技术与解决方案的覆盖范围 |
| technical depth | 技术深度 | 对特定技术的深入掌握程度 |
| business drivers | 业务驱动因素 | 转化为架构特性的业务成功要求 |
| architectural extensibility | 架构可扩充性 | 通过增加功能扩充系统；与 scalability 的负载扩展区分 |
| Frozen Caveman Anti-Pattern | 冰冻穴居人反模式 | 被过往经历固化的担忧左右架构判断 |
| topic | 主题 | 发布订阅消息模型中的目的地 |
| queue | 队列 | 本章点对点消息模型中的目的地 |
| contract | 契约 | 服务所接受的数据与约定 |
| homogeneous / heterogeneous contracts | 同构 / 异构契约 | 所有消费者相同或可按消费者分别定义 |
| programmatic load balancing | 程序化负载均衡 | 通过程序实施的负载均衡 |
| bottleneck trap | 瓶颈陷阱 | 架构师负责关键路径代码而阻塞团队 |
| proof of concept (POC) | 概念验证 | 使用可运行示例验证方案 |
| technical debt story | 技术债务故事 | 纳入迭代的技术债务工作项 |
| architecture story | 架构故事 | 纳入迭代的架构工作项 |
| code review | 代码评审 | 本章作为保持技术参与的一种方法 |
| modularity | 模块化 | 相关代码的逻辑分组，不必物理分离 |
| module / component | 模块 / 组件 | 保留本书对两者的区分 |
| cohesion | 内聚 | 部分应放在一起的关联程度 |
| coupling | 耦合 | 代码元素之间的依赖与连接 |
| connascence | 共变性 | 一方变化要求另一方同步修改以保持正确；不等同于类型系统中的协变 |
| afferent coupling | 传入耦合 | 指向当前代码制品的连接 |
| efferent coupling | 传出耦合 | 当前代码制品指向其他制品的连接 |
| abstractness | 抽象度 | 本版公式与说明存在疑点，见第 3 章译注 |
| instability | 不稳定性 | 传出耦合占传入与传出耦合总和的比例 |
| distance from the main sequence | 到主序列的距离 | 保留原书公式与图示 |
| Lack of Cohesion in Methods (LCOM) | 方法内聚缺失度 | 结构指标，版本定义需要核对 |
| essential complexity | 本质复杂性 | 问题本身带来的复杂性 |
| strength / locality / degree | 强度 / 局部性 / 程度 | 共变性的三个属性 |
| Connascence of Name (CoN) | 名称共变性 | 多组件对名称达成一致 |
| Connascence of Type (CoT) | 类型共变性 | 与时机共变性同用 CoT，按上下文区分 |
| Connascence of Meaning (CoM) | 含义共变性 | 又称约定共变性 CoC |
| Connascence of Position (CoP) | 位置共变性 | 值的顺序需一致 |
| Connascence of Algorithm (CoA) | 算法共变性 | 算法需一致 |
| Connascence of Execution (CoE) | 执行共变性 | 执行顺序重要 |
| Connascence of Timing (CoT) | 时机共变性 | 执行时机重要 |
| Connascence of Values (CoV) | 值共变性 | 相关值必须共同变化 |
| Connascence of Identity (CoI) | 身份共变性 | 多组件引用同一实体 |
| explicit / implicit architecture characteristics | 显式 / 隐式架构特性 | 是否在需求文档或指示中明确给出 |
| operational architecture characteristics | 运维架构特性 | 如性能、可用性、可靠性 |
| structural architecture characteristics | 结构架构特性 | 如模块化、可维护性 |
| cross-cutting architecture characteristics | 横切架构特性 | 跨越类别的设计约束与关注点 |
| accessibility | 无障碍性 | 覆盖具有不同能力与特征的用户 |
| interoperability / compatibility | 互操作性 / 兼容性 | 不直接视为同义词，按上下文区分 |
| usability | 易用性 | 与 learnability 易学性区分 |
| ubiquitous language | 统一语言 | 团队建立一致的领域术语 |
| resilience | 韧性 | 第 4 章“意大利性”例子 |
| safety / security | 安全保障 / 安全性 | 第 4 章表格中区分生命或任务安全与信息安全 |
| architecture kata | 架构 Kata | 用领域场景限时练习设计与权衡 |
| customizability | 可定制性 | 按本地或特定需要调整行为 |
| internationalization (i18n) | 国际化 | 面向不同地区或语言进行设计 |
| sacrificial architecture | 可牺牲架构 | 保留原书称谓，需结合后续背景理解 |
| Ivory Tower Architect | 象牙塔架构师 | 脱离实现团队做架构决策的反模式 |
| performance budget | 性能预算 | 对特定应用部分设定的性能或资源上限 |
| first contentful paint | 首次内容绘制 | 保留本版使用的性能指标名称 |
| first CPU idle | 首次 CPU 空闲 | 本版性能指标名称，不推断当前推荐性 |
| governance | 治理 | 通过规则与反馈影响开发和架构演进 |
| cyclic dependency | 循环依赖 | 组件或包之间形成依赖环 |
| test-driven development (TDD) | 测试驱动开发 | 先写测试，再实现通过测试的代码 |
| chaos engineering | 混沌工程 | 通过模拟故障验证系统承受能力 |
| bounded context | 限界上下文 | DDD 中模型语义的局部边界，保留本书说明 |
| synchronous / asynchronous connascence | 同步 / 异步共变性 | 本书扩展到服务通信的分析概念 |
| independently deployable | 可独立部署 | 架构量子的定义条件之一 |
| domain-driven design (DDD) | 领域驱动设计 | 复杂问题领域的建模与分解方法 |
| technical / domain partitioning | 技术 / 领域划分 | 按技术能力或业务领域组织顶层组件 |
| modular monolith | 模块化单体 | 单一部署单元内部按领域组织模块 |
| Conway’s law | 康威定律 | 系统设计反映组织沟通结构 |
| Inverse Conway Maneuver | 逆康威操作 | 调整团队和组织结构以促进期望架构 |
| entity trap | 实体陷阱 | 机械将实体或数据库关系当作组件与工作流 |
| actor/actions approach | 参与者 / 动作方法 | 从角色及其动作发现组件 |
| event storming | 事件风暴 | 本章用于组件发现，保留本书语境 |
| workflow approach | 工作流方法 | 围绕角色参与的活动组织组件 |
| system of record | 权威记录系统 | 保存并提供权威记录的系统或组件 |
| unitary architecture | 单机一体式架构 | 与单体部署的 monolithic 概念区分 |
| client/server | 客户端 / 服务器 | 常见两层划分 |
| fallacies of distributed computing | 分布式计算谬误 | 关于网络与协作的八项错误假设 |
| circuit breaker | 熔断器 | 对失败或不可用依赖的保护机制 |
| tail latency | 尾延迟 | 分布尾部请求的较高延迟 |
| stamp coupling | 印记耦合 | 传递复合数据结构而消费者只用其中部分 |
| consumer-driven contract (CDC) | 消费者驱动契约 | 本章用于解耦服务数据需求 |
| eventual consistency | 最终一致性 | 数据经过传播后达到一致状态 |
| transaction saga | 事务 Saga | 分布式事务管理方法，具体机制需说明 |
| event sourcing | 事件溯源 | 不与补偿机制自动等同 |
| closed / open layer | 封闭 / 开放层 | 请求不可绕过或可以绕过的层 |
| layers of isolation | 隔离层 | 契约不变时隔离层内部变化 |
| architecture sinkhole | 架构陷坑 | 请求逐层透传而无实质逻辑 |
| mean time to recovery (MTTR) | 平均恢复时间 | 原书讨论单体恢复成本 |
| mock / stub | 模拟 / 存根替代 | 用于隔离测试组件或层 |
| pipeline architecture | 管道架构 | 又称管道与过滤器架构 |
| pipe / filter | 管道 / 过滤器 | 通信通道与处理步骤 |
| producer / transformer / tester / consumer | 生产者 / 转换器 / 测试器 / 消费者 | 本章四类过滤器 |
| telemetry | 遥测 | 服务运行信息 |
| microkernel / plug-in architecture | 微内核 / 插件架构 | 稳定核心与独立插件协作 |
| core system | 核心系统 | 运行所需最小功能或通用流程 |
| plug-in registry | 插件注册表 | 记录插件及访问方式 |
| happy path | 正常路径 | 通用且无特殊异常或定制的处理流程 |
| adapter | 适配器 | 将第三方契约转换为核心标准契约 |
| service-based architecture | 基于服务的架构 | 本书粗粒度领域服务风格，与 SOA、微服务分别讨论 |
| domain service | 领域服务 | 本章指粗粒度独立部署单元，注意与其他语境区分 |
| API facade | API 外观 | 对外统一入口并编排内部请求 |
| orchestration / choreography | 编排 / 协同 | 中央协调与服务间自主协作 |
| service locator pattern | 服务定位器模式 | 根据服务标识定位访问目标 |
| event-driven architecture | 事件驱动架构 | 组件异步接收与处理事件 |
| broker / mediator topology | 代理 / 中介者拓扑 | 无中央工作流控制与中央协调的两类拓扑 |
| initiating / processing event | 初始 / 处理事件 | 启动流程的事件与处理器完成动作后发布的事件 |
| event processor / event channel | 事件处理器 / 事件通道 | 事件驱动架构的处理与通信要素 |
| back pressure | 背压 | 下游处理速度影响上游或积压的反馈机制 |
