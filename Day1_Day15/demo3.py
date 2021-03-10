# -*- coding = utf-8 -*-
# @Time : 2021/3/4 10:45
# @Author : shiki
# @File : demo3.py
# @Software : PyCharm

import random

coin = 1000
while coin > 0:
    print(f"您的余额为：{coin}")
    debt = int(input("您下注的数量为："))
    while debt > coin:
        print("余额不够，请重新下注：", end=" ")
        debt = int(input())
    point1 = random.randint(1, 6) + random.randint(1, 6)
    if point1 == 7 or point1 == 11:
        print(f"您的点数为：{point1}")
        print("玩家获胜！")
        coin += debt
    elif point1 == 2 or point1 == 3 or point1 == 12:
        print(f"您的点数为：{point1}")
        print("庄家获胜！")
        coin -= debt
    else:
        point2 = random.randint(1, 6) + random.randint(1, 6)
        while point2 != 7 and point2 != point1:
            print(f"您的点数为：{point2}")
            point2 = random.randint(1, 6) + random.randint(1, 6)
        if point2 == 7:
            print(f"您的点数为：{point2}")
            print("庄家获胜！")
            coin -= debt
        elif point2 == point1:
            print(f"您的点数为：{point2}")
            print("玩家获胜！")
            coin += debt
print("You Lose!")