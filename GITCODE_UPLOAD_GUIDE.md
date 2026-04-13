# GitCode 上传指南

本文档提供详细的 GitCode 上传步骤。

## 📋 前提条件

- 已有 GitCode 账号（可使用 GitHub 账号登录）
- 已安装 Git
- 已准备好技能代码

## 🚀 上传步骤

### 第一步：在 GitCode 创建新仓库

1. 访问 **https://gitcode.com**
2. 登录你的账号（可使用 GitHub 账号直接登录）
3. 点击右上角 **+** 号，选择 **新建仓库**
4. 填写信息：
   - 仓库名称: `k12-smart-teacher`
   - 仓库描述: `智能老师辅导系统 - K12学生作业批改、错题分析、举一反三练习生成`
   - 选择 **公开**
   - **不要勾选** "使用Readme文件初始化仓库" 等选项
5. 点击 **创建仓库**

### 第二步：关联 GitCode 远程仓库

在终端执行：

```bash
cd ~/.workbuddy/skills/k12-smart-teacher

# 添加 GitCode 远程仓库
git remote add gitcode https://gitcode.com/shellery1988/k12-smart-teacher.git

# 查看远程仓库
git remote -v
```

### 第三步：推送代码到 GitCode

```bash
# 推送到 GitCode
git push gitcode main
```

如果提示输入用户名和密码：
- Username: 你的 GitCode 用户名
- Password: 使用 GitCode Personal Access Token

### 第四步：验证上传成功

访问 `https://gitcode.com/shellery1988/k12-smart-teacher` 查看仓库。

## 🔄 同时推送到 GitHub 和 GitCode

```bash
# 推送到 GitHub
git push origin main

# 推送到 GitCode
git push gitcode main

# 同时推送到两个平台
git push origin main && git push gitcode main
```

## ✅ 完成

现在可以分享技能链接：

```
# GitHub（全球访问）
https://github.com/shellery1988/k12-smart-teacher

# GitCode（国内访问）
https://gitcode.com/shellery1988/k12-smart-teacher
```

国内用户可以通过以下方式安装：

```
安装技能：https://gitcode.com/shellery1988/k12-smart-teacher
```

## 🔧 常见问题

### Q: GitCode 和 GitHub 有什么区别？

A: GitCode 是国内的代码托管平台，国内访问速度更快。两个平台功能基本一致。

### Q: 如何同步两个平台的代码？

A: 修改代码后，分别推送到两个平台：
```bash
git push origin main    # GitHub
git push gitcode main   # GitCode
```

### Q: GitCode 如何生成 Personal Access Token？

A: 访问 GitCode → 设置 → 访问令牌 → 创建新令牌

### Q: 推送时提示权限错误？

A: 需要配置 GitCode 认证：
- 使用 Personal Access Token
- 或配置 SSH 密钥

## 📊 两个平台对比

| 特性 | GitHub | GitCode |
|------|--------|---------|
| 访问速度（国内） | 较慢 | 快 |
| 访问速度（国外） | 快 | 较慢 |
| 账号登录 | GitHub账号 | GitHub/GitCode账号 |
| 免费私有仓库 | ✅ | ✅ |
| Pages服务 | ✅ | ✅ |

**建议：同时推送到两个平台，覆盖国内外用户！**
