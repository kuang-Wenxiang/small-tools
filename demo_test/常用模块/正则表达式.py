"""
re模块
在python中使用正则表达式
http://tool.chinaz.com/regex
"""
# 规则 字符串 从字符串中找到符合规则的内容

"""字符组 :[] 写在中括号中的内容，都出现在下面的某一个字符的位置上都是符合规则的"""
# [0-9] 匹配数字
# [a-z] 匹配小写字母
# [A-Z] 匹配大写字母
# [a-zA-Z0-9]匹配大小写字母加数字
# 顺序必须按照ASCII码的顺序

# 转义符
# \
# \\
# \\w == "\w"

"""元字符"""
# \w  字母、数字、下划线 word[a-zA-Z0-9]
# \W  非字母、数字、下划线
# \d  数字 digit[0-9]
# \D  非数字
# \s  所有的空白符、回车、制表符 space[\n\t ]
# \S  非所有的空白符、回车、制表符
# \t  制表符 table
# \n  换行符、回车
# 全集 [\s\S],[\d\D],[\w\W]
# \b  单词的边界

# ^  匹配字符串的开始
# $  匹配字符串的结束
# .  匹配字符串后面零次或一次（除换行符）贪婪匹配
# ? 匹配字符串后面零次或一次（除换行符）惰性匹配
# * 匹配字符串后面任意数量字符（除换行符）贪婪匹配
# + 匹配字符串后面任意一次或多次（除换行符）贪婪匹配eg:\d+8
# {1,2} 匹配字符串后面1到2次（除换行符）贪婪匹配
# 量词后面加一个?为非贪婪eg:.*?x 匹配非换行符任意次直到遇到x为止
"""量词"""
# + * ？ {n} {n,} {n,m}
# ^[1-9]\d{16}[\dX]|[1-9]\d{14}$ 身份证号码
















