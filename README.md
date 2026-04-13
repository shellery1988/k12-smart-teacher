# K12 Smart Teacher - 智能老师辅导系统

[![Skill](https://img.shields.io/badge/Skill-k12--smart--teacher-blue)](https://github.com/shellery1988/k12-smart-teacher)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

智能老师辅导系统，用于K12学生的作业批改、错题分析、举一反三练习生成。支持小学、初中、高中全学段，涵盖九大学科。

## ✨ 核心功能

- 📋 **作业批改**：自动识别试题并批改，生成详细分析报告
- 🎯 **错题分析**：智能识别薄弱知识点，提供错因分析
- 🎨 **可视化讲解**：用图形、漫画、动画等方式讲解错题
- 📺 **视频推荐**：自动搜索并推荐优质解题视频
- 📝 **举一反三练习**：自动生成专业梯度练习试卷
- 📊 **学习报告**：自动生成学习报告，跟踪学习进度
- 🤖 **智能识别**：自动识别学科和年级

## 📚 支持范围

### 学段覆盖
- ✅ 小学（一年级至六年级）
- ✅ 初中（初一至初三）
- ✅ 高中（高一至高三）

### 学科覆盖
- ✅ 语文、数学、英语
- ✅ 物理、化学、生物
- ✅ 历史、地理、政治

## 🚀 快速安装

本技能支持多种AI开发工具安装，选择适合你的方式：

### 方法一：WorkBuddy 安装

在 WorkBuddy 中执行：

```
安装技能：https://github.com/shellery1988/k12-smart-teacher
```

或手动安装：

```bash
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.workbuddy/skills/k12-smart-teacher
cd ~/.workbuddy/skills/k12-smart-teacher
python3 scripts/quick_setup.py
```

### 方法二：OpenClaw 安装

在 OpenClaw 中执行：

```
安装技能：https://github.com/shellery1988/k12-smart-teacher
```

或手动安装：

```bash
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.openclaw/skills/k12-smart-teacher
cd ~/.openclaw/skills/k12-smart-teacher
python3 scripts/quick_setup.py
```

### 方法三：ClaudeCode 安装

在 ClaudeCode 中执行：

```
安装技能：https://github.com/shellery1988/k12-smart-teacher
```

或手动安装：

```bash
git clone https://github.com/shellery1988/k12-smart-teacher.git ~/.claudecode/skills/k12-smart-teacher
cd ~/.claudecode/skills/k12-smart-teacher
python3 scripts/quick_setup.py
```

### 方法四：通用手动安装

适用于任何支持技能系统的AI工具：

```bash
# 1. 克隆仓库
git clone https://github.com/shellery1988/k12-smart-teacher.git

# 2. 复制到对应工具的技能目录
# WorkBuddy: cp -r k12-smart-teacher ~/.workbuddy/skills/
# OpenClaw:  cp -r k12-smart-teacher ~/.openclaw/skills/
# ClaudeCode: cp -r k12-smart-teacher ~/.claudecode/skills/

# 3. 安装依赖
cd k12-smart-teacher
python3 scripts/quick_setup.py
```

### 📊 安装方式对比

| 平台 | 安装命令 | 技能目录 | 状态 |
|------|---------|---------|------|
| **WorkBuddy** | `安装技能：URL` | `~/.workbuddy/skills/` | ✅ 完全支持 |
| **OpenClaw** | `安装技能：URL` | `~/.openclaw/skills/` | ✅ 完全支持 |
| **ClaudeCode** | `安装技能：URL` | `~/.claudecode/skills/` | ✅ 完全支持 |

**所有平台功能完全一致，依赖自动安装，开箱即用！**

## 🌐 仓库地址

本技能同时发布在以下平台：

| 平台 | 仓库地址 | 适用地区 |
|------|---------|---------|
| **GitHub** | https://github.com/shellery1988/k12-smart-teacher | 全球访问 |
| **GitCode** | https://gitcode.com/shellery1988/k12-smart-teacher | 国内访问 |

**国内用户推荐使用GitCode，访问速度更快！**

## 📖 使用指南

### 首次使用

1. 上传作业或试卷照片
2. 系统自动识别学科和年级
3. 批改并分析错题
4. 生成可视化讲解
5. 推荐优质学习视频
6. 生成举一反三练习

### 持续学习

- 每次练习后自动更新学习档案
- 定期生成学习报告
- 阶段性回顾薄弱知识点

## 🛠️ 依赖说明

### 自动安装的依赖

技能首次加载时会自动安装所有必需依赖：

- **Python**：pillow, requests, python-docx, openpyxl
- **Node.js**：docx
- **系统**（可选）：tesseract, imagemagick

### 手动安装依赖

```bash
# Python 依赖
pip install pillow requests pytesseract python-docx openpyxl

# Node.js 依赖
npm install docx

# macOS 系统依赖
brew install tesseract tesseract-lang imagemagick
```

## 📁 项目结构

```
k12-smart-teacher/
├── SKILL.md                        # 核心技能文档
├── README.md                       # 项目说明
├── LICENSE                         # 许可证
├── scripts/                        # 脚本目录
│   ├── generate_paper.py           # 试卷生成脚本
│   ├── setup_dependencies.sh       # 依赖安装脚本
│   └── quick_setup.py              # 快速安装脚本
├── references/                     # 参考资料目录
│   ├── math_knowledge.md           # 数学知识点库
│   ├── subject_identification.md   # 学科识别指南
│   └── video_resources.md          # 视频资源指南
└── assets/                         # 资源文件目录
    └── paper_template.js           # 试卷模板
```

## 🎯 核心特性

### 1. 多平台支持

本技能支持多种AI开发工具：
- ✅ **WorkBuddy** - 腾讯云AI助手
- ✅ **OpenClaw** - 开源AI开发平台
- ✅ **ClaudeCode** - Anthropic官方开发工具

所有平台功能完全一致，一键安装即可使用。

### 2. 智能识别学科和年级

系统会根据试题内容自动判断学科和年级：
- 分析试题特征（公式、文字、符号等）
- 匹配学科特征库
- 根据难度推断年级

### 3. 可视化讲解

避免枯燥的文字说明，使用生动有趣的方式讲解：
- 图形化展示（流程图、对比图）
- 漫画式讲解（角色对话、故事情节）
- 动画效果（翻页式、渐进展示）

### 4. 视频资源推荐

自动搜索并推荐优质解题视频：
- B站（bilibili）
- 学而思网校
- 洋葱学园
- 猿辅导

### 5. 专业梯度练习

每套练习包含三个层次：
- 🟢 基础巩固（最多3题）
- 🟠 能力提高（最多3题）
- 🟣 拓展挑战（最多2题）

### 6. 学习报告生成

- 单次练习报告
- 阶段总结报告
- 期中/期末仿真训练建议

## 📝 示例

### 上传试卷后

```
用户：上传试卷照片
系统：
1. 自动识别学科：数学
2. 自动识别年级：五年级
3. 批改并分析错题
4. 生成可视化讲解页面
5. 推荐B站讲解视频
6. 生成举一反三练习
7. 提供Word下载
```

## 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

感谢以下平台提供的优质教育资源：
- B站（bilibili）
- 学而思网校
- 洋葱学园
- 猿辅导
- 腾讯课堂

---

**Made with ❤️ for K12 Education**
