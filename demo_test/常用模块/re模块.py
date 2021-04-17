# regex
"""查找"""
import re

"""findall:匹配所有"""
# ret = re.findall('\d+', 'banging245345gagi5ng')  # 正则表达式，带匹配的字符串，flag
# ret = re.findall('\d', 'banging245345gagi5ng')
# print(ret)

"""search：只匹配从左到右的第一个，得到的不是直接的结果，而是一个变量，通过这个变量的group方法来获取结果"""
# ret = re.search("\d+", 'fdfb2df3ds44f56g34645fdf,.')
# print(ret)  # 内存地址，这是一个正则匹配的结果
# print(ret.group())  # 通过ret.group()获取真正的结果

"""match:从头开始匹配，相当于search中的正则表达式加上一个^"""
# ret = re.match('\d+$', '22fb2343hubbub435ff')
# print(ret)

"""split:切割"""
# s = 'alex88tabbi40egon250'
# ret = re.split('\d+', s)
# print(ret)

"""sub:替换"""
# ret = re.sub('\d+', 'H', 'adieus43t3b5begets5')
# print(ret)

"""subn:替换+替换的次数"""
# ret = re.subn('\d+', 'H', 'adieus43t3b5begets5')
# print(ret)

"""compile:节省使用正则表达式解决问题的时间"""
# ret = re.compile('\d+')
# print(ret)
# res = ret.findall('verbs3545fgt66')
# print(res)
# res = ret.search('verbs3545fgt66')
# print(res.group())

"""finditer:节省使用正则表达式解决问题的空间"""
# ret = re.finditer('\d+', 'disused4534nj43n5k3453n')
# print(ret)
# for i in ret:
#     print(i.group())

"""分组优先"""
# s = "<a>wahaha</a>"
# ret = re.findall('>(\w+)<', s)
# print(ret)

"""取消分组优先"""
# s = "<a>wahaha</a>"
# ret = re.findall('>(?:\w+)<', s)
# print(ret)

# ret = re.split('\d+', 'alex23dc45gt')
# print(ret)
# ret = re.split('(\d+)', 'alex23dc45gt')
# print(ret)

"""分组命名"""
# s = "<a>wahaha</a>"
# ret = re.search('>(?P<con>\w+)<', s)
# print(ret.group(1))
# print(ret.group('con'))