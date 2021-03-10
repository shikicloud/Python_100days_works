# -*- coding = utf-8 -*-
# @Time : 2021/3/4 9:46
# @Author : shiki
# @File : demo2.py
# @Software : PyCharm

# 输出斐波那契数列前二十项
# 1 1 2 3 5 8 13 21 34 55
i = 1
j = 1
for n in range(18):
    i, j = j, i+j
    print(j, end="  ")