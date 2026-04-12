# GitHub 上传指南

本文档提供详细的 GitHub 上传步骤。

## 📋 前提条件

- 已有 GitHub 账号
- 已安装 Git
- 已准备好技能代码

## 🚀 上传步骤

### 第一步：在 GitHub 创建新仓库

1. 访问 **https://github.com**
2. 登录你的账号
3. 点击右上角 **+** 号，选择 **New repository**
4. 填写信息：
   - Repository name: `k12-smart-teacher`
   - Description: `智能老师辅导系统 - K12学生作业批改、错题分析、举一反三练习生成`
   - 选择 **Public**
   - **不要勾选** "Add a README file" 等选项
5. 点击 **Create repository**

### 第二步：关联远程仓库

在终端执行（替换 `YOUR_USERNAME` 为你的 GitHub 用户名）：

```bash
cd ~/.workbuddy/skills/k12-smart-teacher

# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/k12-smart-teacher.git

# 查看远程仓库
git remote -v
```

### 第三步：推送代码

```bash
# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 第四步：验证上传成功

访问 `https://github.com/YOUR_USERNAME/k12-smart-teacher` 查看仓库。

## 🔄 更新 README 中的用户名

推送成功后，更新 README.md 中的 `your-username` 为你的实际用户名：

```bash
# 替换 your-username 为实际用户名
sed -i '' 's/your-username/YOUR_USERNAME/g' README.md

# 提交并推送
git add README.md
git commit -m "Update GitHub username in README"
git push
```

## ✅ 完成

现在可以分享技能链接：

```
https://github.com/YOUR_USERNAME/k12-smart-teacher
```

其他人可以通过以下方式安装：

```
安装技能：https://github.com/YOUR_USERNAME/k12-smart-teacher
```

## 🔧 常见问题

### Q: 推送时提示权限错误？

A: 需要配置 GitHub 认证：
- 使用 Personal Access Token (推荐)
- 或配置 SSH 密钥

### Q: 如何更新技能？

A: 修改代码后执行：
```bash
git add .
git commit -m "Update description"
git push
```

### Q: 如何删除远程仓库？

A: 访问仓库 Settings → Danger Zone → Delete this repository
