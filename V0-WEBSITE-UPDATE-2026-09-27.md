# 官网收尾：在现有 v0 项目执行

2026-09-27 06:20 UTC，所有者确认官网在 v0，要求先完成其他外围工作，再交付提示词，由所有者操作官网。本交接不要求再次安装 Vercel、提供 Token 或开放源码仓库；没有声称官网代码已修改或上线。下面内容用于原 humanjudgment.org 项目，不新建项目。

## 提示词

请在当前已经绑定 humanjudgment.org 的 v0 官网项目中，直接完成一次 JEP Core 0.7 的内容、示例、路由与搜索入口收尾。不要另建网站，不要重新设计品牌，不要修改 Prooftask。保留现有字体、颜色、导航、响应式布局与 EN/ZH 切换。完成代码和预览验收后交给我确认，由我在现有项目发布；不要自动发布到生产域名。

### 1．先读现有源码与资料

- [发布快照 -07](https://github.com/hjs-spec/jep-core/tree/main/releases/draft-07/)
- [实现指南](https://github.com/hjs-spec/jep-core/blob/main/docs/IMPLEMENTER-GUIDE.md)
- [当前结构 schema](https://github.com/hjs-spec/jep-core/blob/main/schemas/jep-event.schema.json)
- [本地可运行示例](https://github.com/hjs-spec/jep-agent-sdk#local-create--export--independent-verification)
- [当前交付状态](DELIVERY-CURRENT.md)
- [真实官网核查](WEBSITE-REVIEW-2026-09-27.md)

只修改官网，不修改这些协议仓库或冻结草案。资料不能读取时明确指出，不凭旧页面猜测协议。

### 2．保留正确的页面与协议边界

首页、/protocol、/architecture 的主要内容已经采用 0.7，不要重新做成旧版。全站中英文一致：

- JEP 是关于 Judgment、Delegation、Termination、Verification 的签名事件协议，不是 agent 运行时、判断引擎或法律合规执行平台。
- 协议为 Core 0.7，发布草案为 -07，线格式 `jep` 仍是字符串 `"1"`；软件版本独立。
- 11 个标准顶层成员：`jep,id,verb,who,when,what,aud,ref,ext,ext_crit,sig`。无条件必填七个：`jep,id,verb,who,when,what,sig`；其余依事件/扩展条件判断。不能称 11 个全部必填。
- `who` 是事件声明的主体，`when` 是主体声明的时间，不自动证明身份或可信授时。
- Event Identity 是 `(who,id)`；Event Hash 标识包含签名的准确制品；接收幂等性有接收域边界，不是全球 exactly-once 执行保证。
- Core 不要求顶层 nonce，不定义累计 Validation Levels；整体结果与独立检查分开，未执行的检查不得标为 pass。
- 签名不自动证明事实、授权、法律效力、完整日志、任务完成、付款条件或外部执行。JEP 是个人提交的 IETF Internet-Draft，不称为已获 IETF 批准的标准。

### 3．修正 /developers

删除或替换带 `ref` 数组、`EdDSA` 占位头和假 signature 值的“可用事件”示例。当前 `ref` 是摘要字符串或类型化对象，不是数组；通用签名容器与具体 baseline 分开，不能笼统称对象签名都非法。不得凭空编造签名、公钥或验证成功标记。

本轮最小可靠方案是把主要 Quickstart 换成真实发布版本的本地操作，不在网站实现签名服务：

```sh
git clone --branch v2.1.6 --depth 1 https://github.com/hjs-spec/jep-agent-sdk.git
cd jep-agent-sdk
python -m pip install jep-agent-sdk==2.1.6 jep-core-conformance==0.7.5
python examples/local_roundtrip.py create ./local-evidence
python examples/local_roundtrip.py verify ./local-evidence
jep-validate ./local-evidence/event.json --keys ./local-evidence/keys.json
```

提示使用新虚拟环境；已有输出目录不覆盖。不把历史 `jep-v06-conformance-seed` 与当前 Core 同装。说明产生 `event.json`、`public-key.pem`、`keys.json`，演示私钥不导出。随记录附带的公钥仅演示签名一致性，真实主体绑定需要独立可信来源。不得要求上传真实材料或秘密。

结构示意要明确不是可验签样本。当前实现 baseline 是 JCS + Ed25519 detached JWS，不把其他算法说成本工具已经支持。

默认入口为无需账号/托管 API 的本地创建→导出→独立核验；HTTP 是自行配置地址的替代路径。JavaScript 安装为 `npm install @hjs-api-db/jep-sdk-js@0.7.2`，这是 HTTP 客户端，不是浏览器离线签名器；GitHub 仍为 `hjs-spec/sdk-js`。

开发者区的组合为 Core 0.7.5、Agent SDK 2.1.6、CLI 0.7.2、Python HTTP SDK 0.7.0、JS HTTP SDK 0.7.2、Go HTTP SDK 0.7.2、API 0.8.5、HTTP Quickstart 0.7.0；不要把首页堆成版本清单。

替换编造的通用“规范错误码”清单，链接真实验证器文档，或只列已核对且注明实现/版本范围的示例。不要把 profile/companion 检查列为所有 Core 实现都会执行。

明确：参考 API 可自行部署，维护方正式托管 API 暂未开放。不推荐旧 Hugging Face 作为生产接口，不增加未实现的 Get API Key 或在线调用按钮。

### 4．退役三个旧路由

服务器端永久重定向：`/governance → /architecture`，`/alignment → /architecture`，`/primitives → /protocol`。按现有框架使用 301/308，不能只有前端跳转或隐藏导航。同步真实存在的语言路由，不凭空创建 `/zh`、`/en`，不得循环或跳到不存在的页。

移除旧路由专属模拟、假实时状态和无用代码，保留源码版本历史，不破坏共用组件。检查共用页脚、翻译字典与元数据，移除无依据的“每个动作都由 Sovereign Node 见证”“Zero PII”“No personal data ever touches the protocol”“自动法律合规”“原子 Kill-Switch/自动熔断”“<1.5ms”“100k+ RPS”等能力承诺。不是补一句免责声明后继续作为能力展示；不编造法律条文、政府认可、客户案例或性能测试。

### 5．搜索入口

保持 apex 到 www 的正常跳转，不改 DNS/证书/域名绑定。根据实际 Next.js 版本和路由结构补 `robots.txt`、`sitemap.xml`，采用 `app/robots.ts`、`app/sitemap.ts` 或等效静态方式，不新增后台、数据库、轮询或付费工具。

允许公开文档抓取并指向正确 sitemap；不要用 robots 屏蔽已重定向页导致爬虫看不到重定向；保留真正私有路由的保护。sitemap 仅列当前真实可索引页，不包含退役路由、预览域名或虚构语言 URL。`lastModified` 使用真实修改时间，无法确定则省略。

为保留页设置独立、准确的 title/description/canonical 与分享元数据，canonical 使用 www 正式域名；保留预览 noindex。EN/ZH 按现有实现同步；仅实际独立语言 URL 使用相应 hreflang。

参考现有框架官方文档：[metadata](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)、[sitemap](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)。不要为了本轮收尾升级框架。

### 6．验收后交给我发布

真实运行现有类型检查、lint、测试和生产构建，按 package.json 的实际脚本执行，不编造通过数量或大幅更换依赖。检查桌面和手机的菜单、语言切换、代码复制、代码块横向滚动、链接和正文阅读；整页不能横向溢出。

验证三条永久跳转、目标页、robots 文本、sitemap XML、canonical、代码示例和假能力文案清除。无法执行时明确未验证，不以构建通过代替线上验收。

给出实际修改文件、测试与预览结果和仍需我点击发布的事项。仅更新原有项目与预览，由我确认后发布到原生产站；不得新建付费资源、部署 JEP API、创建数据库或更改 Prooftask。
