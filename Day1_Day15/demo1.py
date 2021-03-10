# -*- coding = utf-8 -*-
# @Time : 2021/3/4 0:23
# @Author : shiki
# @File : demo1.py
# @Software : PyCharm

# 将输入的整数反转(牢记牢记牢记！)
num = int((input("num = ")))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num *10 + num % 10
    num = num // 10
print(reverse_num)

