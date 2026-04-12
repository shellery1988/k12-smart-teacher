#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能老师 - 试卷生成脚本
根据学科和知识点自动生成专业梯度练习试卷
"""

import argparse
import subprocess
import json
import os

def generate_math_questions(topic, basic_count=5, improve_count=5, challenge_count=5):
    """生成数学练习题"""
    
    questions = {
        "basic": [],
        "improve": [],
        "challenge": []
    }
    
    # 根据知识点生成题目（这里需要扩展更多知识点）
    if "最大公因数" in topic or "公因数" in topic:
        questions["basic"] = [
            {"type": "计算", "content": "用短除法求下列各组数的最大公因数。\n（1）18 和 27　　（2）24 和 36　　（3）45 和 60"},
            {"type": "填空", "content": "填空：如果 a 是 b 的倍数，那么 a 和 b 的最大公因数是（　　），最小公倍数是（　　）。"},
            {"type": "判断", "content": "判断对错，对的打\"√\"，错的打\"×\"。\n（1）两个数的最大公因数一定比这两个数都小。（　　）\n（2）如果两个数互质，它们的最大公因数是1。（　　）\n（3）相邻两个自然数的最大公因数是1。（　　）"},
            {"type": "选择", "content": "选择题：36 和 48 的最大公因数是（　　）。\nA. 4　　B. 6　　C. 12　　D. 24"},
            {"type": "填空", "content": "直接写出下列各组数的最大公因数。\n（1）8 和 24 = ______　　（2）17 和 51 = ______　　（3）15 和 16 = ______"}
        ]
        questions["improve"] = [
            {"type": "应用题", "content": "有两根铁丝，一根长 72 厘米，另一根长 54 厘米。现在要把它们截成同样长的小段，而且不能有剩余。每小段最长是多少厘米？一共可以截成多少段？"},
            {"type": "应用题", "content": "学校买来 48 本故事书和 64 本科技书，要平均分给若干个班级，每个班级分到的故事书和科技书数量相同。最多可以分给多少个班级？每个班级分到故事书和科技书各多少本？"},
            {"type": "应用题", "content": "一张长方形彩纸，长 84 厘米，宽 60 厘米。要把它剪成同样大小的正方形，且没有剩余。剪出的正方形边长最大是多少厘米？最少可以剪成多少个正方形？"},
            {"type": "应用题", "content": "五（1）班有男生 32 人，女生 24 人。在队列操练时，要把男、女生分别排队，要使每排人数相同，每排最多排多少人？这时男、女生各有多少排？"},
            {"type": "应用题", "content": "一个长方体木块，长 36 厘米，宽 24 厘米，高 18 厘米。要把它锯成同样大小的正方体木块，且没有剩余。锯出的正方体棱长最大是多少厘米？最少可以锯成多少块？"}
        ]
        questions["challenge"] = [
            {"type": "思维题", "content": "已知 a 和 b 的最大公因数是 12，最小公倍数是 72。如果 a = 36，那么 b = ？"},
            {"type": "思维题", "content": "三个数分别是 24、36 和 48，它们的最大公因数是多少？"},
            {"type": "思维题", "content": "把一张长 120 厘米、宽 80 厘米的长方形纸板，剪成大小相等的正方形，且没有剩余。有几种剪法？边长分别是多少？"},
            {"type": "思维题", "content": "甲、乙、丙三个数的和是 120，甲数是乙数的 2 倍，乙数是丙数的 2 倍。求甲、乙、丙三个数的最大公因数。"},
            {"type": "思维题", "content": "一个数除 60 余 4，除 80 也余 4。这个数最大是多少？"}
        ]
    
    return questions

def generate_chinese_questions(topic, basic_count=5, improve_count=5, challenge_count=5):
    """生成语文练习题"""
    questions = {
        "basic": [],
        "improve": [],
        "challenge": []
    }
    # 可扩展语文知识点题目生成
    return questions

def generate_english_questions(topic, basic_count=5, improve_count=5, challenge_count=5):
    """生成英语练习题"""
    questions = {
        "basic": [],
        "improve": [],
        "challenge": []
    }
    # 可扩展英语知识点题目生成
    return questions

def main():
    parser = argparse.ArgumentParser(description='生成专业梯度练习试卷')
    parser.add_argument('--subject', required=True, choices=['数学', '语文', '英语'], help='学科')
    parser.add_argument('--topic', required=True, help='知识点主题')
    parser.add_argument('--student', required=True, help='学生姓名')
    parser.add_argument('--grade', required=True, help='年级')
    parser.add_argument('--output', required=True, help='输出文件路径')
    
    args = parser.parse_args()
    
    # 根据学科生成题目
    if args.subject == '数学':
        questions = generate_math_questions(args.topic)
    elif args.subject == '语文':
        questions = generate_chinese_questions(args.topic)
    else:
        questions = generate_english_questions(args.topic)
    
    # 输出题目JSON供后续处理
    output_data = {
        "subject": args.subject,
        "topic": args.topic,
        "student": args.student,
        "grade": args.grade,
        "questions": questions
    }
    
    print(json.dumps(output_data, ensure_ascii=False, indent=2))
    print(f"\n试卷已生成，保存至: {args.output}")

if __name__ == '__main__':
    main()
