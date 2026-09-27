# JEP 0.7：需要你完成的配置

日期：2026-09-27。Core 的 PyPI 授权与发布已经完成；不要再次上传、删除旧包或新建 PyPI Token。本轮开发与发行验收见 [交付记录](DELIVERY-2026-09-27.md)。

## 1．npm 首次发布及自动发布授权（命名空间更新）

当前决定：使用已有 npm 账号 **`hjs-api-db`**，包名 **`@hjs-api-db/jep-sdk-js`**，软件版本 **0.7.2**。GitHub 源码仓库仍是 **`hjs-spec/sdk-js`**。不再申请 npm 的 `hjs-spec` 用户/组织；不转换 `hjs-api-db`，不改 `jep-eth`，不动 `hjs-client` 或 `jep-snap`。

[SDK #12](https://github.com/hjs-spec/sdk-js/pull/12) 已更新包元数据、导入/安装说明、测试和工作流。运行时代码与类型声明不变，协议仍是 Core 0.7；旧 0.7.1 安装包保持原样。旧交付记录中的 0.7.1 测试是其原组合证据，不自动代表新包已通过 npm 发布验收。

### 先发布真实安装包，再配置 Trusted Publisher

从 [GitHub v0.7.2](https://github.com/hjs-spec/sdk-js/releases/tag/v0.7.2) 获取 `hjs-api-db-jep-sdk-js-0.7.2.tgz`。不要给旧 tarball 改文件名冒充新包，不需要空壳占位包。

在本机安装当前 Node.js LTS；使用 `hjs-api-db` 的已验证邮箱账号并启用 npm 双重验证。下载目录打开 PowerShell，逐条执行：

```powershell
npm.cmd login --auth-type=web --registry=https://registry.npmjs.org/
npm.cmd whoami --registry=https://registry.npmjs.org/
```

只有 `whoami` 返回 **`hjs-api-db`** 才执行：

```powershell
npm.cmd publish .\hjs-api-db-jep-sdk-js-0.7.2.tgz --access public --registry=https://registry.npmjs.org/
npm.cmd view @hjs-api-db/jep-sdk-js@0.7.2 version dist.integrity --registry=https://registry.npmjs.org/
```

密码、验证码、恢复码、Token、带令牌的登录链接都不发送到聊天。首次本地发布没有 GitHub OIDC provenance，不能声称已有。npm 上已有同版本时先核对完整性，不重复上传或删除重建。

### 首次发布成功后的填写表

进入 [新包设置](https://www.npmjs.com/package/@hjs-api-db/jep-sdk-js/access) → Trusted publishing → GitHub Actions：

| 字段 | 填写值 |
|---|---|
| Organization or user | `hjs-spec`（这里填 GitHub 所有者，不是 npm 账号） |
| Repository | `sdk-js` |
| Workflow filename | `release.yml` |
| Environment name | 留空，不填写 Any |
| Allowed actions | 允许直接 `npm publish`，以匹配工作流 |

工作流使用 Node 24、GitHub 托管 runner 与 `id-token: write`，不再使用旧 `NPM_TOKEN` 回退。首次发布及授权之后，未来的新版本可按该路径自动发布；保存配置并不等于已经完成一次 OIDC 发布验收。

**不要重跑旧的 0.7.1 失败任务**：旧运行仍携带旧命名空间。首次手动发布 0.7.2 后，也不要再次上传同一版本来测试 OIDC。需要 registry-only 恢复时，`registry.yml` 要有自己的独立授权，不能使用仅授权 `release.yml` 的信任关系。

首次发布后，独立核对 npm 版本、下载 tarball 的 SHA-256/SHA-512 与 GitHub 原件、在干净目录安装并导入新包。之后正常安装命令为 `npm install @hjs-api-db/jep-sdk-js@0.7.2`。未完成前，GitHub tarball 可直接安装；不宣称 npm 已可用。

参考：[SDK 发布说明](https://github.com/hjs-spec/sdk-js/blob/main/PUBLISHING.md)、[npm 公开 scoped 包](https://docs.npmjs.com/creating-and-publishing-scoped-public-packages/)、[npm Trusted Publisher](https://docs.npmjs.com/trusted-publishers/)。

## 2．Hugging Face 生产 API

用途：提供托管的在线签名/验证服务。仅使用本地 Core/Agent SDK 时可以暂不部署。此处列的是当前部署脚本要求；本轮没有读取秘密值、替换身份或启动生产部署。

打开 [Space Settings](https://huggingface.co/spaces/yuqiangJEP/jep-api/settings)，进入 Variables and secrets。

| 类型 | 名称 | 填什么 |
|---|---|---|
| Variable | `JEP_DEPLOYMENT_MODE` | `production` |
| Secret | `JEP_DATABASE_URL` | 已批准的生产 PostgreSQL 连接串；确认数据库/数据归属、网络和 TLS，不要填临时测试库 |
| Secret | `JEP_SIGNING_TOKEN` | 已批准的调用签名接口访问凭据；它不是 HF Token，也不是签名私钥 |
| Secret | `JEP_KEYRING_JSON` | 已批准的 Ed25519 密钥环 JSON；保持既有签名身份和历史公钥，不临时造新钥匙来通过检查 |

密钥环和 Vault 两条路径选一条。已经使用 Vault 时，不填 `JEP_KEYRING_JSON`，改配：

| 类型 | 名称 | 填什么 |
|---|---|---|
| Variable | `JEP_VAULT_ADDR` | HTTPS Vault 地址 |
| Variable | `JEP_VAULT_KEY` | 已批准的非派生 Ed25519 Transit key 名称 |
| Variable | `JEP_VAULT_KID_PREFIX` | 与既有签名身份一致的 kid 前缀 |
| Secret | `JEP_VAULT_TOKEN` | 对相应 Transit key 具有必要权限的凭据 |

需要自定义 Transit mount / namespace / CA 时，先按仓库部署说明核对后再配置；默认材料不代替实际基础设施方案。不要同时配置本地密钥环和 Vault。

可在自己的安全环境使用以下“结构示例”整理现有密钥环，尖括号是占位符，不能直接粘贴为生产凭据：

```json
{
  "active_kid": "<现有并获批准的签名 key id>",
  "keys": [
    {
      "kid": "<与 active_kid 一致>",
      "kty": "OKP",
      "crv": "Ed25519",
      "x": "<既有 32 字节公钥的无填充 Base64URL>",
      "d": "<与该公钥匹配的既有 32 字节私钥 seed 的无填充 Base64URL>"
    }
  ]
}
```

历史公钥应继续保留在 keys 中，通常不需要旧私钥 d。不得把这个实际填好私钥的 JSON 提交 GitHub 或发到聊天。

字段来源：[部署预检脚本](https://github.com/hjs-spec/jep-api/blob/main/scripts/deploy_hf.py)、[密钥加载与校验](https://github.com/hjs-spec/jep-api/blob/main/keys.py)。

配置后先执行 `scripts/deploy_hf.py --check-only`（现有 check-hf 工作流也可使用），只看配置名称/模式，不上传或重启。预检成功只说明名称齐全；密钥、公钥匹配、数据库连接与服务状态还需要实际启动验收。

部署使用已测试 API 软件 0.8.4、Core `jep-core-0.7`、源码 `0ed259f8f137f57c8122487ba44e0dcfce5bc172`；核验 `/health` 返回以上三项。再用批准的专用测试上下文检查未授权拒绝、签名及历史验证、重启后的公钥/幂等状态持久化，不以一次健康检查代替全部生产验收。

交回时只需确认：生产数据库已确定；现有签名身份已确认；上述 Variable/Secret 名称已配置；选择密钥环还是 Vault。不要提供秘密值。

## 不需要做的事

不重新提交 IETF -07；不批量发布旧实验包的 post1；不删除历史 0.6 包/签名；不改 Prooftask；不为当前本地验证配置生产数据库或密钥。
