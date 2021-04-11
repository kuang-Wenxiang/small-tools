import random

"""取随机小数"""
# print(random.random())  # 取0-1之间的小数
# print(random.uniform(10, 20)) # 取X-Y之间的小数

"""取随机整数"""
# print(random.randint(1, 2))  # [1,2]
# print(random.randrange(1, 2))  # [1,2)
# print(random.randrange(1, 200, 2))  # [1,200)中的奇数

"""从一个列表中随机抽取值"""
# la = ['a', 'b', 'c', 'd', 'e', 'a']
# print(random.choice(la))
# print(random.sample(la, 2))

"""打乱一个列表的顺序"""
# la = ['a', 'b', 'c', 'd', 'e', 'a']
# random.shuffle(la)
# print(la)


"""举例：验证码"""
# def code(n=6, alpha=True):
#     s = ''
#     for i in range(n):
#         res = str(random.randint(0, 9))
#         if alpha:
#             alpha_upper = chr(random.randint(65, 90))
#             alpha_lower = chr(random.randint(97, 122))
#             res = random.choice([res, alpha_upper, alpha_lower])
#         s += res
#     return s
#
#
# print(code(6))
# print(code(6, False))
# print(code(4, False))
