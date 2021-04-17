"""验证码
1、四位数字
2、六位数字
3、六位数字加字母
"""
import random

# def code(n=6):
# #     s = ''
# #     for i in range(n):
# #         nums = random.randint(0, 9)
# #         s += str(nums)
# #     return s
# #
# #
# # print(code(4))
# # print(code(6))
# # print(code())

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
