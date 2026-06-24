# K12 Smart Teacher - 智能老师辅导系统

[![Skill](https://img.shields.io/badge/Skill-k12--smart--teacher-blue)](https://skillhub.cn)
[![Version](https://img.shields.io/badge/Version-1.0.1-brightgreen)](https://skillhub.cn)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-WorkBuddy%20%7C%20OpenClaw%20%7C%20ClaudeCode-orange)](https://skillhub.cn)

> K12智能老师辅导系统，支持作业批改、错题分析、可视化讲解、举一反三练习生成。覆盖小学/初中/高中全学段，九大学科。数学专项题库更丰富，其他学科提供基础模板练习，可按教材和错题继续细化。

---

## ✨ 核心功能

| 功能 | 描述 |
|------|------|
| 📋 **作业批改** | 自动识别试题并批改，生成详细分析报告 |
| 🎯 **错题分析** | 智能识别薄弱知识点，提供错因分析 |
| 🎨 **可视化讲解** | 图形、漫画、动画等方式讲解错题（禁止纯文字） |
| 📺 **视频推荐** | 自动搜索并推荐优质B站/学而思等解题视频 |
| 📝 **梯度练习** | 自动生成基础/提高/挑战三层次练习 |
| 📊 **学习报告** | 自动生成学习报告，跟踪知识点掌握进度 |
| 🤖 **智能识别** | 自动识别学科和年级，无需手动指定 |
| 📄 **练习文件** | 支持Markdown/JSON；安装 python-docx 后支持Word |

---

## 📚 支持范围

### 学段覆盖
- ✅ 小学（一年级至六年级）
- ✅ 初中（初一至初三）
- ✅ 高中（高一至高三）

### 学科覆盖与当前能力

| 学科 | 当前能力 |
|------|----------|
| 数学 | 专项题更丰富，最大公因数等知识点可直接生成带答案练习 |
| 语文/英语 | 支持字词、阅读、语法、写作等基础模板练习 |
| 物理/化学/生物 | 支持概念、实验、现象分析、探究题模板 |
| 历史/地理/政治 | 支持材料分析、概念梳理、开放表达模板 |

> 想要更贴合教材，请补充：年级、教材版本、章节名、错题照片或原题文字。

---

## 🗣️ 怎么开口使用

可以直接这样说：

```text
孩子五年级，数学最大公因数总错。请先讲明白，再出8题以内练习，最后给答案。
```

```text
这张作业帮我批改。请按：错题、错因、可视化讲解、推荐视频、举一反三练习 的顺序来。
```

```text
生成一份初二物理“浮力”的练习。如果Word生成不了，就给我可打印的Markdown版。
```

---

## ⚠️ 能力边界

- 作业照片识别依赖图片清晰度；看不清时会请你补图或输入题目。
- Word文件依赖 `python-docx`；缺少依赖时会自动降级生成Markdown，不会直接中断。
- 九大学科都能生成基础练习，但非数学专项题需要教材、章节或原题材料才能更精准。
- 不替孩子直接完成作业；会先讲解思路，再给答案和同类练习。

---

## 🚀 快速安装

### SkillHub 安装（推荐）

在支持 SkillHub 的 AI 工具中执行：
```
安装技能：k12-smart-teacher
```

### 手动安装

```bash
# WorkBuddy
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.workbuddy/skills/k12-smart-teacher

# OpenClaw
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.openclaw/skills/k12-smart-teacher

# ClaudeCode
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.claudecode/skills/k12-smart-teacher

# 安装依赖（首次使用，自动安装）
cd k12-smart-teacher && python3 scripts/quick_setup.py
```

---

## 🎯 核心理念

> **理解优先于练习！**

教学流程：**错题分析 → 可视化讲解 → 视频推荐 → 举一反三练习**

绝对不能跳过"错题讲解"直接生成练习题。

---

## 📁 文件结构

```
k12-smart-teacher/
├── SKILL.md                    # 核心技能指令文档
├── README.md                   # 项目说明（本文件）
├── LICENSE                     # MIT 许可证
├── scripts/
│   ├── generate_paper.py       # 试卷生成脚本
│   ├── setup_dependencies.sh   # 依赖安装脚本(Bash)
│   └── quick_setup.py          # 快速安装脚本(Python)
├── references/
│   ├── math_knowledge.md       # 数学知识点库
│   ├── subject_identification.md  # 学科识别指南
│   └── video_resources.md      # 视频资源推荐指南
└── assets/                     # 资源文件目录
```

---

## 🧪 直接生成练习文件

```bash
python3 scripts/generate_paper.py \
  --subject 数学 \
  --topic 最大公因数 \
  --student 小明 \
  --grade 五年级 \
  --output 练习/小明-最大公因数.docx
```

支持输出：
- `.docx`：安装 `python-docx` 后生成Word
- `.md`：可打印Markdown，依赖最少
- `.json`：方便其他工具继续处理

如果 `.docx` 依赖不可用，脚本会自动生成同名 `.md` 文件，并给出中文提示。

---

## 🛠️ 依赖说明

首次使用前可执行依赖检查和安装：

- **Python**：pillow, requests, python-docx, openpyxl
- **Node.js**：docx
- **系统（可选）**：tesseract（OCR），imagemagick

```bash
python3 scripts/quick_setup.py
```

---

## ❓ 常见问题

**Q：生成Word失败怎么办？**  
A：脚本会自动降级生成Markdown。需要Word时，先运行 `python3 scripts/quick_setup.py` 安装依赖。

**Q：为什么语文/英语/物理题比较通用？**  
A：这些学科目前提供基础模板。补充教材版本、课文、章节或错题原文后，可以改写成更贴合的练习。

**Q：视频推荐打不开怎么办？**  
A：优先推荐国内平台。若搜索失败，会提供B站可复制关键词，方便手动查找。

---

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)

---

## 👤 联系方式

- 📧 **邮箱**：shelleryliu@163.com
- 💬 **微信**：naskfcode
- 🔗 **GitHub**：https://github.com/shellery1988/k12-smart-teacher
- 🔗 **GitCode**：https://gitcode.com/shellery1988/k12-smart-teacher

---

**Made with ❤️ for K12 Education**
