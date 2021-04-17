# 序列：列表 元组 字符串 bytes

# 把其他的数据类型转换成字符串 bytes 序列化的过程

# dic = {'1': '2'}
# print(str(dic), dic)
# print([str([1, 2, 3]), [1, 2, 3]])

# import json
# import pickle
import json
# dic = {'key': 'value', 'key2': 'value2'}
# ret = json.dumps(dic)  # 序列化
# print(dic)
# print(dic, type(dic))
# print(ret)
# print(ret, type(ret))
#
# res = json.loads(ret)  # 反序列化
# print(res)
# print(res, type(res))

"""问题一"""
# dic = {1: 'aaa', 2: 'bbb'}
# ret = json.dumps(dic)
# print(ret)
# print(json.loads(ret))
"""问题二"""
# dic = {1: [1, 2, 3], 2: (4, 5, 'aa')}
# ret = json.dumps(dic)
# print(ret)
# print(json.loads(ret))
"""问题三"""
# s = {1, 2, 'aaa'}
# json.dumps(s)
"""问题四"""
# json.dumps({(1, 2, 3): 123})

# json能够处理的数据类型是有限的：字符串、列表、字典、数字
# 字典中的key只能是字符串

