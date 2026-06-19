# aizjewelry.com 托管与域名绑定指南

## 第一步：准备 Cloudflare 账户
1. 访问 [dash.cloudflare.com](https://dash.cloudflare.com/) 注册一个免费账户。
2. 点击左侧菜单的 **Workers & Pages** -> **Create application** -> **Pages** -> **Upload assets**。
3. 给你的项目起名（例如 `aiz-jewelry`），点击 **Create project**。

## 第二步：上传网站文件
1. 将我为你生成的 `website` 文件夹中的三个文件（`index.html`, `style.css`, `script.js`）拖拽到上传区域。
2. 点击 **Deploy site**。现在你已经获得了一个以 `.pages.dev` 结尾的临时地址。

## 第三步：在阿里云修改 DNS (核心步骤)
1. 登录阿里云域名控制台。
2. 找到 `aizjewelry.com`，选择“修改 DNS 服务器”。
3. 在 Cloudflare 中，点击 **Add a site**，输入 `aizjewelry.com`。
4. Cloudflare 会给你两个 DNS 服务器地址（例如 `ns1.cloudflare.com` 和 `ns2.cloudflare.com`）。
5. 将这两个地址填回阿里云的 DNS 服务器设置中，保存。

## 第四步：在 Cloudflare 绑定自定义域名
1. 在 Cloudflare Pages 的项目设置中，选择 **Custom domains**。
2. 点击 **Set up a custom domain**，输入 `www.aizjewelry.com` 和 `aizjewelry.com`。
3. 按照 Cloudflare 的指引自动激活 HTTPS（免费 SSL 证书）。

## 完成！
你的网站现在已通过 Cloudflare 的全球 CDN 节点进行分发，欧美和澳大利亚的客户访问速度将非常快，且完全免费托管。
