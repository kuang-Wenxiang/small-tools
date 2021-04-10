lst = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
"""
简单实现二分查找
"""
# n = 111
# left = 0
# right = len(lst) - 1
# count = 1
# while left <= right:
#     middle = (left + right) // 2
#     if n < lst[middle]:
#         right = middle - 1
#     elif n > lst[middle]:
#         left = middle + 1
#     else:
#         print(count)
#         print(middle)
#         break
#     count = count + 1
# else:
#     print("不存在")
"""
递归实现二分法
"""


def func(n, left, right):
    middle = (left + right) // 2
    if left <= right:
        if n < lst[middle]:
            right = middle - 1
            return func(n, left, right)
        elif n > lst[middle]:
            left = middle + 1
            return func(n, left, right)
        else:
            print("找到了！")
            return middle
    else:
        print("不存在！")
        return -1


print(func(125, 0, len(lst) - 1))
