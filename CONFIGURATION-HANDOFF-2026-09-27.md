# JEP 外围配置交接：当前状态

更新日期：2026-09-27。本页替代此前的首次发布操作清单；[原文按原字节保留](CONFIGURATION-HANDOFF-2026-09-27-HISTORICAL.md)，仅用于历史复现，不要再照旧清单操作。

## 已完成，不要重复操作

Core 的 PyPI 发布及公开下载验收已经完成。JavaScript 包 `@hjs-api-db/jep-sdk-js@0.7.2` 已完成真实首发、独立哈希对比和不带凭据的安装验证。npm 账号为 `hjs-api-db`；GitHub 源码仓库为 `hjs-spec/sdk-js`，两个命名空间不必相同。

所有者已确认 npm 的 `release.yml` Trusted Publisher 已添加，临时 npm Token 和 GitHub `NPM_BOOTSTRAP_TOKEN` 已清理。这是所有者确认，不声称后台已独立读取这些设置，也不声称已完成实际 OIDC 上传。下一次正常软件发版时再验证，不重发 0.7.2 或另造版本来测试。

当前发行组合已纳入 Core #34，完成 Linux/Windows/macOS 公开下载安装、原件哈希和签名互操作验证。API #16 已关闭随 Release 自动部署；JS #15 已退役一次性首发工作流；历史报告和发行原件不改写。详细证据见[当前交付入口](DELIVERY-CURRENT.md)。

## 托管 API 暂缓

保留 API 源码、测试、发行件和自行部署能力；不要求配置数据库、签名私钥、HF Token 或购买硬件。此前独立新建的 Railway API、数据库和磁盘已清理，活动资源清单已核对。原 Hugging Face Space 未改动，不作为当前正式服务推荐。

未来明确决定提供托管服务时，重新确定费用、运维责任、数据库、网络、客户权限隔离、签名身份、备份恢复和验收计划。按届时的[部署说明](https://github.com/hjs-spec/jep-api/blob/main/DEPLOYMENT.md)执行，不复用已删除试运行环境的凭据，不默认复用 Prooftask。

## 官网由所有者在 v0 操作

06:20 UTC 所有者确认官网在 v0，并要求先完成其他工作，最后提供提示词。执行路径已经改为：[原官网项目的完整 v0 提示词](V0-WEBSITE-UPDATE-2026-09-27.md)。不需要再次安装/授权 Vercel，不索要 Token，也不新建官网项目。

[核查记录](WEBSITE-REVIEW-2026-09-27.md)中的工具访问限制是当时的检查记录，不是现在要求所有者重复连接的操作清单。本轮已经完成实时页面核查和提示词交付；官网修改、预览确认及生产发布仍由所有者执行，尚未声称上线修复。

## 留到正常发版验收的事项

- npm 免 Token 发布：下一次计划内新版本实际上传时验证。
- PyPI 页面：README 绝对链接和项目链接已经在源码修复，随下一次正常发行更新；既有版本页面和发行原件未被覆盖。

目前没有需要新增账号、Token、数据库或服务器的步骤。密码、验证码、恢复码和真实密钥均不通过聊天传递。

[当前交付入口](DELIVERY-CURRENT.md) · [集成目录](PROJECTS.md) · [v0 官网提示词](V0-WEBSITE-UPDATE-2026-09-27.md)
