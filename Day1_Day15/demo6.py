# -*- coding = utf-8 -*-
# @Time : 2021/3/8 21:36
# @Author : shiki
# @File : demo6.py
# @Software : PyCharm

# 录入5个学生3门课程的考试成绩，计算每个学生的平均分和每门课的平均分。
"""
# 创建一个3*5的列表存放学生成绩信息
grades = [[0]*3 for _ in range(5)]

# 导入学生成绩
for i in range(5):
    for j in range(3):
        grades[i][j] = int(input(f"Please input student{i+1}'s grade in class{j+1}:"))

stu_grade = [0, 0, 0, 0, 0]
# 计算每个学生的平均分
for i in range(5):
    for j in range(3):
        stu_grade[i] += grades[i][j]
    print(f"学生{i+1}的平均成绩为：{stu_grade[i]/3:.1f}")

class_grade = [0, 0, 0]
# 计算每科成绩的平均分
for i in range(3):
    for j in range(5):
        class_grade[i] += grades[j][i]
    print(f"课程{i+1}的平均成绩为：{class_grade[i]/5:.1f}")
"""

"""
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 用生成式创建嵌套的列表保存5个学生3门课程的成绩
scores = [[0] * len(courses) for _ in range(len(names))]
# 录入数据
for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()
print('-' * 5, '学生平均成绩', '-' * 5)
# 计算每个人的平均成绩
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')
"""

# 录入5个学生3门课程的考试成绩，计算每个学生的平均分和每门课的平均分。

# 创建学生、课程和成绩列表
students = ["a", "b", "c", "d", "e"]
courses = ["C1", "C2", "C3"]
grades = [[0]*3 for _ in range(5)]

# 导入学生成绩
for i, student in enumerate(students):
    print("*"*10)
    for j, course in enumerate(courses):
        grades[i][j] = int(input(f"学生{student}的{course}课的成绩为："))

# 计算学生的平均分
for i, student in enumerate(students):
    print("*"*10)
    stu_ave = sum(grades[i])/3
    print(f"学生{student}的平均成绩为：{stu_ave}")
# 计算每门课的平均分
for i, course in enumerate(courses):
    print("*"*10)
    course_score = [grade[i] for grade in grades]
    print(course_score)
    course_ave = sum(course_score)/5
    print(f"课程{course}的平均分为：{course_ave}")