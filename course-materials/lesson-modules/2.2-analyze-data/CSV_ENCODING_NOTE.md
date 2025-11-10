# CSV文件编码说明

## 编码格式

所有CSV文件使用 **UTF-8 with BOM** 编码格式。

## 为什么使用UTF-8 BOM?

1. **兼容性**: Excel在Windows系统上默认使用系统编码(GBK),如果CSV是纯UTF-8编码,中文会显示为乱码
2. **UTF-8 BOM**: 在文件开头添加特殊标记(﻿),告诉Excel这是UTF-8文件
3. **跨平台**: 在Mac、Windows、Linux上都能正确显示中文

## 如何验证编码

```bash
# 查看文件前几行(应该能看到中文)
head -3 activation-funnel-q4.csv

# Python读取测试
python3 -c "
import csv
with open('activation-funnel-q4.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    print(next(reader))
"
```

## 生成新CSV文件

如果需要重新生成CSV文件:

```bash
python3 generate_data.py
```

generate_data.py 已配置为自动使用 `encoding='utf-8-sig'`

## 在不同工具中打开

- **Excel**: 直接双击打开,中文显示正常
- **Python**: 使用 `encoding='utf-8-sig'` 读取
- **Google Sheets**: 直接导入,自动识别
- **VS Code**: 直接打开,显示正常

## 文件列表

- `activation-funnel-q4.csv` - 激活漏斗数据
- `singtech-usage-data-q4.csv` - K歌APP使用数据  
- `user-survey-responses.csv` - 用户调查反馈
- `onboarding-experiment-results.csv` - 新手引导实验数据
