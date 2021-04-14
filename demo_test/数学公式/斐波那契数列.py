# 获取用户输入数据
terms = int(input("请输入你要的位数："))

# 第一和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if terms <= 0:
    print("请输入一个正整数。")
elif terms == 1:
    print("斐波那契数列：")
    print(n1)
elif terms == 2:
    print("斐波那契数列：")
    print(n1, ",", n2)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < terms:
        if count != terms - 1:  # 去除最后一个","
            nth = n1 + n2
            print(nth, end=" , ")
            # 更新值
            n1 = n2
            n2 = nth
            count += 1
        else:
            nth = n1 + n2
            print(nth)
            break
"""
按最大的数进行筛选
"""
# num = int(input("请输入最大的数："))
# n1 = 0
# n2 = 1
# nth = 0
# while nth < num:
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
# else:
#     print(n1)

