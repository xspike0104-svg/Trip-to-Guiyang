---
name: "pdf-smart-tool-cn"
description: PDF智能处理工具 v2.1 | PDF Smart Tool. 支持PDF转换、OCR识别、合并拆分、数字签名、批量处理、水印添加、加密解密。触发词：PDF、转换、识别。
homepage: https://clawhub.com/skills/pdf-smart-tool-cn
---

# PDF智能处理工具

## 功能
- PDF文本提取
- PDF内容分析
- PDF转文本

## 使用方法

### 方法1：使用Node.js（推荐）

```javascript
const fs = require('fs');

// 使用 pdf-parse 模块（需先安装）
// npm install --prefix <工作目录> pdf-parse
```

### 方法2：使用Python（如果已安装pdfplumber）

```python
import pdfplumber

def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
```

### 方法3：使用内置的pdf工具

使用 `pdf` 工具读取PDF文件：
- 单个PDF：`pdf(pdf="<文件路径>", prompt="要提取的内容描述")`
- 多个PDF：`pdfs(["<文件1>", "<文件2>"], prompt="要提取的内容描述")`

## 示例

### 提取PDF全文
```
请读取这个PDF文件： C:\Users\pc\Desktop\example.pdf
```

### 分析PDF内容
```
分析这个PDF的主要内容：
```

## 注意事项

1. PDF文件路径不能包含中文（可能有问题）
2. 如果是扫描件PDF（无文字层），需要OCR处理
3. 大型PDF可能需要更长时间处理
