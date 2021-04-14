# lst = [{"mm": 222}, {"mm": 333}, {"mm": 111}]
#
# func1 = lambda a1: a1 ** a1
#
# print(func1(3))

# name = ["a", "b", "c"]
# print(list(map(lambda x: x + "_sb", name)))


# l = [{'name': 'alex'}, {'name': 'y'}]
# print(list(map(lambda x: x['name'] + '_sb', l)))

# share = {
#     'IBM': 36.6,
#     'lenora': 23.2,
#     'oboe': 21.2,
#     'ocean': 10.2
# }
#
# print(list(filter(lambda x: x > 20, share.values())))
# print(list(filter(lambda x: share[x] > 20, share)))


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

def code(n=6, alpha=True):
    s = ''
    for i in range(n):
        res = str(random.randint(0, 9))
        if alpha:
            alpha_upper = chr(random.randint(65, 90))
            alpha_lower = chr(random.randint(97, 122))
            res = random.choice([res, alpha_upper, alpha_lower])
        s += res
    return s


print(code(6))
print(code(6, False))
print(code(4, False))

"""发红包
1、输入红包数量、钱数
2、拼手气红包（注意每个人的概率是公平的）
"""
