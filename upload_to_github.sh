#!/bin/bash
# K12 Smart Teacher - GitHub 上传脚本
# 使用方法：bash upload_to_github.sh

echo "=========================================="
echo "  K12 Smart Teacher - GitHub 上传工具"
echo "=========================================="
echo ""

# 配置信息
GITHUB_USERNAME="shellery1988"
REPO_NAME="k12-smart-teacher"
REPO_URL="https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

echo "📋 仓库信息："
echo "   用户名：${GITHUB_USERNAME}"
echo "   仓库名：${REPO_NAME}"
echo "   仓库地址：${REPO_URL}"
echo ""

echo "⚠️  请确保已在 GitHub 上创建仓库："
echo "   1. 访问 https://github.com/new"
echo "   2. Repository name: ${REPO_NAME}"
echo "   3. 选择 Public"
echo "   4. 不要勾选任何初始化选项"
echo "   5. 点击 Create repository"
echo ""
read -p "已创建仓库？按回车继续..." 

# 进入技能目录
cd ~/.workbuddy/skills/k12-smart-teacher || exit 1

echo ""
echo "📦 准备推送代码到 GitHub..."

# 查看当前状态
echo ""
echo "📊 Git 状态："
git status -s

# 推送到 GitHub
echo ""
echo "🚀 推送代码..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "🎉 你的技能已上传到："
    echo "   ${REPO_URL}"
    echo ""
    echo "📖 其他人可以这样安装："
    echo "   安装技能：${REPO_URL}"
    echo ""
else
    echo ""
    echo "❌ 推送失败！"
    echo ""
    echo "可能的原因："
    echo "1. GitHub 仓库未创建"
    echo "2. 网络连接问题"
    echo "3. 认证问题（需要 Personal Access Token）"
    echo ""
    echo "解决方法："
    echo "1. 访问 https://github.com/new 创建仓库"
    echo "2. 检查网络连接"
    echo "3. 配置 Git 认证："
    echo "   git config --global credential.helper store"
    echo ""
fi
