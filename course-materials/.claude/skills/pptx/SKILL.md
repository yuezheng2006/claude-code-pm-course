---
name: pptx
description: 从 markdown 文档创建 PowerPoint 演示文稿。当用户需要将战略文档、PRD 或分析转换为专业的幻灯片演示文稿以进行利益相关者演示时使用此技能。
---

# PowerPoint 演示文稿创建技能

您可以从 markdown 文档创建专业的 PowerPoint 演示文稿（.pptx 文件）。此技能旨在帮助产品经理将他们的书面工作转换为适合高管的幻灯片演示文稿。

## 功能

- 将 markdown 文档转换为 PowerPoint 演示文稿
- 根据内容结构创建适当的幻灯片布局
- 应用专业的格式和设计
- 生成标题幻灯片、内容幻灯片和摘要幻灯片
- 支持战略演示、PRD 和分析文档

## 何时使用此技能

在用户需要以下情况时使用此技能：
- 从战略文档创建高管演示文稿
- 将书面分析转换为幻灯片演示文稿
- 向利益相关者展示 PRD 或功能规范
- 为领导层审查生成专业幻灯片

## 如何创建演示文稿

创建演示文稿时，遵循此工作流程：

### 1. 分析源文档

阅读 markdown 文档并识别：
- 应该成为幻灯片的主要部分
- 关键点和支持细节
- 视觉层次和流程
- 高管摘要内容

### 2. 设计幻灯片结构

规划演示文稿结构：
- **标题幻灯片**：文档标题、日期、背景
- **高管摘要**：关键要点（1-2 张幻灯片）
- **主要内容幻灯片**：每个主要部分一张幻灯片
- **详细信息幻灯片**：支持信息，分解以提高可读性
- **结束幻灯片**：摘要、下一步或行动号召

### 3. 创建演示文稿

使用 Python 和 `python-pptx` 库生成 .pptx 文件：

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# 创建演示文稿对象
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# 定义可重用的布局
def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[0])  # 标题布局
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    return slide

def add_content_slide(prs, title, content_items):
    slide = prs.slides.add_slide(prs.slide_layouts[1])  # 标题和内容布局
    slide.shapes.title.text = title

    # 将内容添加为要点
    body = slide.placeholders[1].text_frame
    for item in content_items:
        p = body.add_paragraph()
        p.text = item
        p.level = 0
    return slide

def add_section_slide(prs, section_title):
    slide = prs.slides.add_slide(prs.slide_layouts[2])  # 章节标题布局
    slide.shapes.title.text = section_title
    return slide

# 示例：创建幻灯片
add_title_slide(prs, "战略标题", "演示日期")
add_section_slide(prs, "第 1 部分：诊断")
add_content_slide(prs, "关键发现", [
    "发现 1：此处描述",
    "发现 2：此处描述",
    "发现 3：此处描述"
])

# 保存演示文稿
prs.save('output.pptx')
```

### 4. 格式指南

应用专业格式：

**排版：**
- 标题字体：幻灯片标题 44pt，章节标题 54pt
- 正文：主要内容 18-24pt，详细信息 16pt
- 使用无衬线字体（Calibri、Arial 或 Helvetica）

**布局：**
- 每张幻灯片最多 3-5 个要点
- 比较时使用 2 列布局
- 将密集内容分解到多张幻灯片
- 留白以提高可读性

**内容原则：**
- 每张幻灯片一个关键想法
- 使用主动、简洁的语言
- 要点应该在结构上平行
- 包含幻灯片编号以供参考

**特殊幻灯片类型：**

*战略幻灯片：*
- 诊断 → 指导政策 → 行动结构
- 使用视觉层次显示关系
- 突出权衡和关键决策

*路线图幻灯片：*
- 按季度/月份的时间线视图
- 分组相关计划
- 标注依赖关系

*指标幻灯片：*
- 当前 vs. 目标性能
- 使用简单的表格或图表（口头描述，实现为格式化文本）
- 包含成功标准

## 输出

创建演示文稿后：
1. 使用描述性名称保存 .pptx 文件
2. 向用户确认文件位置
3. 总结幻灯片结构（幻灯片数量和关键部分）
4. 注意为演示格式简化或重新构建的任何内容

## 依赖项

此技能需要 `python-pptx` 库。如果未安装，请指导用户安装：

```bash
pip install python-pptx
```

## 最佳实践

- **高管优先**：从高管可以在 2 分钟内阅读的摘要幻灯片开始
- **可扫描**：每张幻灯片应该在 10 秒内理解
- **可操作**：以明确的下一步或需要的决策结束
- **专业**：在整个过程中使用一致的格式
- **上下文感知**：根据受众调整正式程度和细节

## 使用示例

**用户请求**："从我的战略文档创建幻灯片演示文稿"

**您的工作流程**：
1. 阅读战略文档
2. 识别关键部分（诊断、指导政策、行动等）
3. 规划约 12-15 张幻灯片涵盖战略
4. 使用 python-pptx 生成 Python 代码
5. 创建 .pptx 文件
6. 确认创建并总结结构

## 注意事项

- 对于本课程，演示文稿用于将产品经理文档（战略、PRD、分析）转换为适合利益相关者的格式
- 专注于清晰度和专业性，而不是视觉设计的复杂性
- 如有疑问，使用具有清晰层次的简单布局
- 目标是使书面工作适合演示，而不是创建营销材料
