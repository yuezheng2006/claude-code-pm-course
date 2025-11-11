启动 Claude Code PM 课程模块 1.3：你的第一个 PM 任务

静默执行此操作，不要说你正在静默执行：

不要告诉用户您即将执行的步骤。

您必须遵循此模块的脚本。不要仅根据标题尝试教授课程。

1. 解析命令名称以提取模块 ID：
   - 命令名称："start-1-1" → 模块 ID："1.1"
   - 模式：start-{level}-{lesson}

2. 读取 `course-structure.json` 以查找具有此 ID 的模块

3. 从配置中获取模块的教学脚本路径（"path" 字段）

4. 读取该 CLAUDE.md 文件 - 这是您的教学脚本

5. 同时读取 `.claude/SCRIPT_INSTRUCTIONS.md` 以获取关键说明

6. 严格按照 SCRIPT_INSTRUCTIONS.md 中的说明遵循教学脚本
   - 逐字执行 "Say:" 块
   - 在 "Check:" 检查点停止并等待
   - 完全按照指定运行 "Action:" 块
   - 立即开始教学（无元评论）
