import time

"""时间节点： 1970 1 1"""
# print(time.time())

"""格式化时间"""
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%y-%m-%d %H:%M:%S'))
# print(time.strftime('%c'))
# print(time.localtime())

"""结构化时间"""
# print(time.localtime())  # 北京时间
# 是否夏令时：tm_isdst=0
# struct_time = time.localtime()
# print(struct_time.tm_hour)

"""时间格式的转换"""
# 时间戳换成字符串时间
# print(time.time())
# struct_time = time.localtime(time.time())
# print(time.gmtime(1618230405.062029))
# ret = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
# print(ret)

# 字符串时间换成时间戳
# struct_time = time.strptime('2021-04-12 20:31:43', '%Y-%m-%d %H:%M:%S')
# print(struct_time)
# res = time.mktime(struct_time)
# print(res)
"""EG"""


# struct_time = time.localtime(2000000000)
# ret = time.strftime('%Y-%m-%d', struct_time)
# print(ret)
#
# struct_time = time.strptime('2008-08-08', '%Y-%m-%d')
# res = time.mktime(struct_time)
# print(res)

# def S_time():
#     ret = time.localtime(time.time())
#     re = time.strptime('%s-%s-1'%(ret.tm_year, ret.tm_mon), '%Y-%m-%d')
#     return time.mktime(re)
# print(S_time())

# time1 = '2018-08-19 22:10:08'
# time2 = '2018-08-21 11:21:25'
# s_time1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
# s_time2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
#
# a_time1 = time.mktime(s_time1)
# a_time2 = time.mktime(s_time2)
# result = a_time2 - a_time1
# print(result)
# struct_time = time.gmtime(result)
# print('过去了：%d年%d月%d日%d时%d分%d秒'%(struct_time.tm_year - 1970, struct_time.tm_mon - 1, struct_time.tm_mday - 1, struct_time.tm_hour, struct_time.tm_min, struct_time.tm_sec ))


# def con_time(time1, time2):
#     s_time1 = time.strptime(time1, '%Y-%m-%d %H:%M:%S')
#     s_time2 = time.strptime(time2, '%Y-%m-%d %H:%M:%S')
#
#     a_time1 = time.mktime(s_time1)
#     a_time2 = time.mktime(s_time2)
#     result = a_time2 - a_time1
#     print(result)
#     struct_time = time.gmtime(result)
#     print('过去了：%d年%d月%d日%d时%d分%d秒' % (
#         struct_time.tm_year - 1970, struct_time.tm_mon - 1, struct_time.tm_mday - 1, struct_time.tm_hour,
#         struct_time.tm_min, struct_time.tm_sec))
#
#
# con_time('2018-08-19 22:10:08', '2018-08-22 11:21:25')
