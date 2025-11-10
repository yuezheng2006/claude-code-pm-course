# 部署到Vercel


## 快速部署（推荐）

### 选项1：通过Vercel控制台部署

1. **推送到GitHub**（如果还没有推送）：
   ```bash
   cd /Users/carl/claude-code-pm-course
   git add website/
   git commit -m "添加Nextra文档网站"
   git push origin main
   ```

2. **访问Vercel**：
   - 访问 https://vercel.com/new
   - 使用GitHub登录
   - 点击"Import Project"
   - 选择您的仓库：`yuezheng2006/claude-code-pm-course`

3. **配置构建设置**：
   - **根目录**：`website`
   - **框架预设**：Next.js
   - **构建命令**：`npm run build`（默认即可）
   - **输出目录**：`out`
   - **安装命令**：`npm install`（默认即可）

4. **部署**：
   - 点击"Deploy"
   - 等待约2-3分钟构建完成
   - 您的网站将在 `https://your-project.vercel.app` 上线

5. **自定义域名**（可选）：
   - 在Vercel控制台中，进入Settings → Domains
   - 添加您的自定义域名
   - 按照DNS指示进行配置

## 选项2：通过Vercel CLI部署

```bash
# 全局安装Vercel CLI
npm install -g vercel

# 进入网站目录
cd /Users/carl/claude-code-pm-course/website

# 登录Vercel（仅首次）
vercel login

# 部署到预览环境
vercel

# 部署到生产环境
vercel --prod
```

## 部署内容

您的构建站点包含：
- ✅ 所有课程内容（20个页面）
- ✅ 左侧边栏导航
- ✅ 右侧目录导航
- ✅ 客户端搜索（Pagefind）
- ✅ 公司背景部分
- ✅ 所有图片
- ✅ 响应式移动端布局
- ✅ 快速静态站点（无需服务器）

## 部署后操作

部署完成后：

1. **测试网站**：
   - 检查所有导航链接是否正常工作
   - 测试搜索功能
   - 验证图片是否正确加载
   - 在移动端进行测试

2. **使用上线URL更新README**

3. **分享链接**！

## 更新内容

部署后更新网站内容：

1. 编辑 `/lesson-modules/` 中的 REFERENCE_GUIDE.md 文件
2. 运行转换脚本：
   ```bash
   cd /Users/carl/claude-code-pm-course/website
   ./convert-content.sh
   ```
3. 本地构建和测试：
   ```bash
   npm run build
   npm run preview  # 本地测试
   ```
4. 提交并推送：
   ```bash
   git add .
   git commit -m "更新课程内容"
   git push
   ```
5. Vercel将自动重新构建和重新部署！

## 故障排除

### Vercel构建失败
- 检查Vercel控制台中的构建日志
- 确保将 `website/` 设置为根目录
- 验证Node.js版本（应为18+）

### 搜索功能不工作
- Pagefind在 `postbuild` 脚本中运行
- 检查构建输出中是否存在 `/pagefind/` 目录
- 清除浏览器缓存

### 图片无法加载
- 图片应位于 `/public/images/` 中
- 在MDX文件中引用为 `/images/filename.png`
- 检查浏览器控制台是否有404错误

## 环境变量

无需配置！这是一个静态站点，没有后端或密钥。

## 费用

**Vercel免费套餐包含：**
- 无限制部署
- 每月100 GB带宽
- 自动HTTPS
- 自定义域名
- PR的预览部署

您的静态文档站点将轻松适应免费套餐。

---

**准备好部署了吗？** 请按照上面的选项1（Vercel控制台）操作 - 这是最简单的方式！🚀

