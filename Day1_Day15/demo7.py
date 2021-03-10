# -*- coding = utf-8 -*-
# @Time : 2021/3/8 21:51
# @Author : shiki
# @File : demo7.py
# @Software : PyCharm

# 计算指定的年月日是这一年的第几天
# 创建一个函数判断该年份是否是闰年
def leaf_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 1


def year_month_day_info(year, month, day):
    # 创建一个存入普通年份日期信息的列表
    years = [[i] * 2 for i in range(12)]
    days_for_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index, months in enumerate(years):
        years[index][1] = days_for_months[index]

    # 对用户输入的年份进行判断
    if leaf_year(year) == 1:
        years[1][1] = 29

    # 创建一个变量存放天数信息
    days = 0
    for i in range(month - 1):
        days += years[i][1]
    days += day
    return days


print("-" * 20)
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入号数："))
print("-" * 20)

days = year_month_day_info(year, month, day)
print(f"{year}年{month}月{day}日是这一年的第{days}天。")
