# JEP 0.7：需要你完成的配置

日期：2026-09-27。Core 的 PyPI 授权与发布已经完成；不要再次上传、删除旧包或新建 PyPI Token。本轮开发与发行验收见 [交付记录](DELIVERY-2026-09-27.md)。

## 1．npm 发布授权

用途：让 JavaScript SDK 可通过 npm 安装；它不阻塞 Python Core/Agent SDK 的本地使用。

在 npmjs.com 登录拥有 `@hjs-spec/jep-sdk-js` 发布管理权限的账户，进入该包 Settings → Trusted publishing，添加 GitHub Actions 发布者。

| 字段 | 填写值 |
|---|---|
| Organization or user | `hjs-spec` |
| Repository | `sdk-js` |
| Workflow filename | `release.yml` |
| Environment name | 留空，不填写 Any |
| Allowed actions | 允许直接 `npm publish`，以匹配当前工作流 |

当前仓库已使用 Node 24、GitHub 托管 runner 与 `id-token: write`。不需要把 npm Token 发给助手。npm 要求 npm CLI ≥11.5.1、Node ≥22.14.0；新授权的默认 stage 权限不等于允许当前直接发布命令。保存后只能说明配置已登记，实际发布时才会验证。

参考：[npm 官方 Trusted Publisher 文档](https://docs.npmjs.com/trusted-publishers/)；[实际仓库发布流程](https://github.com/hjs-spec/sdk-js/blob/main/.github/workflows/release.yml)。

配置完成后，交回“授权已保存”或不含秘密的截图即可。恢复时只重跑 [原运行](https://github.com/hjs-spec/sdk-js/actions/runs/36243899535) 中失败的 npm 任务，不重建 GitHub Release。验收包括注册表版本 0.7.1、实际下载 tarball 与 GitHub SHA-256 一致、干净目录安装和测试。

包名或权限页面不可见时先确认 npm 组织及包权限，不改包名、不删除现有版本。所有旧 Token 的撤销应在 OIDC 真正发布成功后另行确认。

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
