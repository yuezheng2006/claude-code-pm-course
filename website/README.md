# Claude Code for Product Managers - 文档网站

这是基于 Nextra 的 Claude Code for Product Managers 课程文档网站。

## 开发

```bash
# 安装依赖
npm install

# 运行开发服务器
npm run dev

# 打开 http://localhost:3000
```

## 构建

```bash
# 构建静态网站
npm run build

# 构建输出将在 `out/` 目录中
# Pagefind 会在构建后自动索引内容
```

## 部署到 Vercel

### 选项 1：通过 Vercel 仪表板连接

1. 访问 [vercel.com](https://vercel.com) 并登录
2. 点击 "Add New Project"
3. 导入 GitHub 仓库：`yuezheng2006/claude-code-pm-course`
4. 将根目录设置为 `website`
5. 框架预设：Next.js
6. 构建命令：`npm run build`
7. 输出目录：`out`
8. 部署！

### 选项 2：通过 Vercel CLI 部署

```bash
# 安装 Vercel CLI
npm i -g vercel

# 从 website 目录部署
cd website
vercel

# 生产环境
vercel --prod
```

## 项目结构

```
website/
├── pages/               # 所有内容页面 (MDX)
│   ├── company-context/ # SingTech 公司信息
│   ├── getting-started/ # 模块 0.0-0.2
│   ├── fundamentals/    # 模块 1.1-1.7
│   ├── advanced/        # 模块 2.1-2.3
│   ├── _app.jsx         # Next.js 应用包装器
│   ├── _meta.ts         # 导航配置
│   ├── index.mdx        # 首页
│   └── search.mdx       # 带 Pagefind 的搜索页面
├── public/
│   └── images/          # 课程图片
├── next.config.mjs      # Next.js 配置
├── theme.config.tsx     # Nextra 主题配置
└── package.json         # 依赖项
```

## 内容更新

内容会自动从主课程的 `lesson-modules/` 目录转换。要更新：

1. 编辑 `/lesson-modules/` 中的 REFERENCE_GUIDE.md 文件
2. 运行转换脚本：`./convert-content.sh`
3. 构建并部署

## 技术栈

- **Next.js 14** - 静态网站生成
- **Nextra 3** - 文档主题
- **Pagefind** - 客户端搜索
- **MDX** - 支持 JSX 组件的 Markdown

## 链接

- **在线网站:** [部署后更新]
- **课程仓库:** https://github.com/yuezheng2006/claude-code-pm-course
- **Nextra 文档:** https://nextra.site
- **Pagefind 文档:** https://pagefind.app
