# Vercel 部署设置

## 在 Vercel 仪表板中使用的确切设置

在 Vercel 上导入项目时，请使用以下确切设置：

### 项目设置
```
项目名称: claude-code-pm-course (或您喜欢的任何名称)
```

### 构建和开发设置
```
框架预设:     Next.js
根目录:       website
构建命令:     npm run build
输出目录:     out  
安装命令:     npm install
```

### 重要提示

1. **根目录必须是 `website`** - 这很关键！
2. 所有其他设置应该会自动检测正确
3. 不要添加自定义的 `vercel.json` 文件
4. Node.js 版本: 18.x 或更高版本（应该会自动检测）

## 如果构建仍然失败

查看构建日志中的错误。常见问题：

### 错误："Cannot find module" 或 "Module not found"
- 检查所有文件是否已提交到 git
- 验证 `node_modules` 是否在 `.gitignore` 中

### 错误："_meta.json not supported"
- 已修复 - 确保您从 main 分支拉取了最新代码
- 应该只有 `_meta.ts` 文件，没有 `_meta.json`

### 错误：frontmatter 中的 "YAML parsing error"
- 已修复 - 所有 frontmatter 都使用单引号
- 检查代码块外是否有任何 `<` 或 `>` 符号

### 构建成功但网站是空白的
- 检查输出目录是否设置为 `out`
- 验证构建后 `/out` 目录是否包含 HTML 文件

## 本地测试

要测试 Vercel 将运行的确切构建：

```bash
cd /Users/carl/claude-code-pm-course/website
rm -rf .next out node_modules
npm install
npm run build

# 检查 out/ 目录是否有内容：
ls -la out/
```

如果本地可以工作，在 Vercel 上也应该可以工作。

## 分享错误

如果仍然失败，请分享：
1. Vercel 构建设置的截图
2. 从构建日志中复制/粘贴错误信息
3. 我会立即修复！
