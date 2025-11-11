# CLAUDE.md

此文件为Claude Code（claude.ai/code）在处理此仓库代码时提供指导。

## 仓库概览

这是一个双用途仓库，用于Claude Code面向产品经理课程：

1. **course-materials/** - 面向学生的交互式课程内容
2. **website/** - Next.js文档站点（部署到Vercel，域名ccforpms.com）

学生下载course-materials/作为zip文件，解压后从该文件夹运行`claude`，输入`/start-1-1`开始学习。

## 课程架构：配置驱动系统

**本课程使用配置驱动架构，以最大化灵活性来添加/重新排序模块。**

### 单一真理来源：course-structure.json

所有模块定义都位于`course-materials/course-structure.json`中。此文件控制：
- 课程结构和模块顺序
- 斜杠命令路由（所有斜杠命令都相同 - 它们读取配置以了解要加载哪个教学脚本）
- 网站导航（在构建时从配置生成）
- 教学脚本导航（模块读取配置以了解接下来是什么）

### 工作原理

**斜杠命令：**
- 所有10个斜杠命令（`/start-1-1`到`/start-2-3`）都是相同的
- 它们解析自己的命令名称（例如："start-1-2" → 模块"1.2"）
- 它们读取`course-structure.json`来找到模块的教学脚本路径
- 它们加载并执行该教学脚本

**教学脚本：**
- 在每个模块的结尾，脚本读取`course-structure.json`
- 它们动态确定接下来是什么
- 它们告诉学生下一个模块的正确斜杠命令

**网站导航：**
- `website/pages/fundamentals/_meta.ts`和`website/pages/advanced/_meta.ts`导入配置
- 导航在构建时从`course-structure.json`生成

### 添加或重新排序模块

要添加新模块或重新排序现有模块：

1. **编辑`course-materials/course-structure.json`** - 添加/移动模块定义
2. **创建新的模块文件夹和文件**（如果添加新模块）
3. **完成！** 其他一切都会自动更新：
   - 斜杠命令正确路由（它们都是相同的）
   - 教学脚本引用正确的"下一个"模块（它们读取配置）
   - 网站导航更新（在构建时从配置生成）

**无需：**
- ❌ 重命名文件夹
- ❌ 更新单个斜杠命令文件
- ❌ 编辑现有教学脚本
- ❌ 手动更新网站`_meta.ts`文件

**示例：在当前1.3和1.4之间插入模块1.4：**

只需编辑`course-structure.json`添加新的模块定义，一切都会自动级联。旧的1.4（agents）文件夹可以保持名为`1.4-agents` - 配置将逻辑ID（1.5）映射到物理路径（1.4-agents）。

### 优势

- ✅ 在不接触现有文件的情况下添加模块
- ✅ 通过编辑一个JSON文件重新排序模块
- ✅ 网站和课程材料自动保持同步
- ✅ 课程结构有一个单一真理来源
- ✅ 课程演进的最大灵活性

## 关键：在打开此仓库时

**除非明确要求，否则不要主动设置、构建或安装任何东西**。README.md包含了关于此的具体警告：

- ❌ 不要运行`npm install`
- ❌ 不要运行`npm run build`
- ❌ 不要进行设置更改
- ✅ 等待明确的指示

这是一个交互式课程仓库。用户（或学生）将指导需要做什么。

## 常用命令

### 发布管理工作流

**更新课程内容时：**

1. **对course-materials/中的文件进行更改**
   - 编辑`course-materials/lesson-modules/`中的模块
   - 更新`course-materials/company-context/`中的公司背景
   - 修改`course-materials/.claude/agents/`中的代理
   - 等等

2. **提交并推送至main：**
   ```bash
   git add -A
   git commit -m "更新模块1.3的新示例"
   git push origin main
   ```

3. **创建新发布：**
   ```bash
   # 使用新版本号运行发布脚本
   ./scripts/create-release.sh v1.0.1

   # 使用新zip创建GitHub发布
   gh release create v1.0.1 releases/complete-course.zip \
     --title "v1.0.1 - 更新模块1.3" \
     --notes "- 修复模块1.3中的拼写错误\n- 为模块2.1添加新示例"
   ```

4. **更新网站（如需要）：**
   - 主页显示"Latest: v1.0.0"
   - 在`website/pages/index.mdx`第128行更新：
   ```markdown
   **👉 [下载课程材料](...latest/download/complete-course.zip)** - 获取完整课程（最新版本：v1.0.1）
   ```

**GitHub发布的工作原理：**
- `/releases/latest/download/complete-course.zip` - 始终指向最新发布
- 使用此URL的学生自动获取最新版本
- 您可以创建任意数量的发布（v1.0.1、v1.0.2、v1.1.0等）
- 旧发布在它们的特定版本URL中仍然可用

**语义化版本指南：**
- `v1.0.X` (补丁) - 错误修复、拼写错误、对现有内容的微小更新
- `v1.X.0` (次要) - 新模块、新功能、对现有内容的重大添加
- `vX.0.0` (主要) - 完全重构、破坏性更改

**快速参考命令：**
```bash
# 1. 更新内容，提交，推送
git add -A && git commit -m "..." && git push origin main

# 2. 创建新发布zip
./scripts/create-release.sh v1.0.1

# 3. 发布到GitHub
gh release create v1.0.1 releases/complete-course.zip \
  --title "v1.0.1 - 描述" \
  --notes "更改内容"
```

就是这样！您网站中的`/releases/latest/` URL将自动指向最新的发布。

### 网站开发

**本地开发：**
```bash
cd website
npm install
npm run dev
```

**生产构建：**
```bash
cd website
npm run build
```

构建过程：
1. `next build` - 在website/out/中创建静态导出
2. `next-sitemap` - 生成sitemap.xml和robots.txt
3. `pagefind` - 为静态站点构建搜索索引

**预览生产构建：**
```bash
cd website
npm run preview
```

### 部署

网站在推送到main分支时自动部署到Vercel（ccforpms.com）。无需手动部署。

### 分析

**Google Analytics：**
- 测量ID：`G-XBF1JD68VY`
- 实现位置：`website/theme.config.tsx`（第44-55行）
- 跟踪：页面浏览量、访客、流量来源、地域数据、设备类型、滚动深度、外链点击
- 验证：访问网站 → 检查Google Analytics实时仪表板

**下载跟踪：**
- 课程材料下载（通过模块0.2的curl）由GitHub内置的发布下载统计跟踪
- 检查下载次数：GitHub仓库 → Releases选项卡，或通过`gh api repos/yuezheng2006/claude-code-pm-course/releases`
- Google Analytics不会跟踪这些下载（它们绕过网站）

## 仓库架构

### 课程材料 (course-materials/)

**结构：**
- `lesson-modules/` - 模块1和模块2的交互式课程
- `company-context/` - 练习中使用的SingTech公司参考材料
- `.claude/` - 驱动课程的斜杠命令、代理和教学脚本

**斜杠命令：**
位于`course-materials/.claude/commands/`，这些是指导学生完成模块的教学脚本：
- `/start-1-1`、`/start-1-2`等用于模块1课程
- `/start-2-1`、`/start-2-2`等用于模块2课程

**教学脚本行为：**
当用户在course-materials/文件夹中输入斜杠命令时，阅读`course-materials/.claude/SCRIPT_INSTRUCTIONS.md`了解执行教学脚本的关键规则。主要要点：
- 教学脚本必须逐字遵循（"Say:"块要逐字逐句）
- "Check:"点是关卡 - 停止并等待学生响应
- "Action:"块包含确切的命令
- 绝不打破第四面墙或说"我已经读过脚本" - 立即开始教学
- 所有示例文件使用.md扩展名（不是.txt），以便与Obsidian配合使用

### 网站 (website/)

**技术栈：**
- Next.js 14，支持静态导出（`output: 'export'`）
- Nextra（文档主题）
- Pagefind（静态搜索）
- Vercel（托管）

**页面结构：**
```
website/pages/
  getting-started/     - 模块0内容（安装、设置）
  fundamentals/        - 模块1内容
  advanced/           - 模块2内容
  company-context/    - SingTech参考（从站点地图中排除）
  index.mdx           - 首页
  _meta.ts            - 导航结构
```

**关键文件：**
- `theme.config.tsx` - Nextra主题配置（logo、页脚、SEO、导航）
- `next.config.mjs` - Next.js配置（静态导出、图片优化）
- `next-sitemap.config.js` - 站点地图生成（排除/company-context/*）

**SEO配置：**
网站在theme.config.tsx中具有全面的SEO：
- Open Graph标签
- Twitter卡片
- Google网站验证
- 通过frontMatter的每页自定义元数据
- 结构化数据支持

### 内部文档 (docs/)

不包含在面向学生的材料中的规划文档：
- `GITHUB_RELEASES_PLAN.md` - 发布策略文档
- `SEO_IMPLEMENTATION_SPEC.md` - SEO规范

## 文件扩展名约定

所有课程示例文件必须使用`.md`扩展名（不是`.txt`），因为：
- 学生使用Obsidian来可视化课程文件（在模块1.2中教授）
- Obsidian无法显示.txt文件
- 这在SCRIPT_INSTRUCTIONS.md中强制执行

## Git工作流

**忽略的文件（.gitignore）：**
- Obsidian工作区文件（个人设置）
- 发布产物（releases/、*.zip）
- 构建输出（node_modules/）
- 大多数.json文件（除了package.json、tsconfig.json）
- 大多数.png文件（除了website/public/**/*.png）

**分支：**
主分支是`main` - 用于拉取请求。

## 网站主题定制

网站使用青色配色方案（`primaryHue: 169`），默认深色主题。页脚包含CC BY-NC-ND 4.0许可证归属。

## 课程理念

本课程通过动手实践教导产品经理使用Claude Code。课程内容本身通过Claude Code交付，创造了一种元学习体验，让学生通过使用工具来学习工具。
