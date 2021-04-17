# name
# Traceback (most recent call last):
#   File "C:/Users/Administrator/gitPH/small-tools/demo_test/基础知识/异常处理.py", line 2, in <module>
#     name
# NameError: name 'name' is not defined
"""
错误的回溯：Traceback
文件的位置+错误的位置
错误类型(错误的类型是有限的)+具体的错误提示
"""
"""找错误的方法：
倒着从最后（非源码）向上找的最后一行
"""

"""
多分支异常处理：
从下向上的代码知道找到一个和报错类型相符的分支就执行这个分支中的代码，然后直接退出分支
"""

"""万能异常:应该永远放在异常处理的最后一个"""
# def func():
#     name
#
# try:
#     func()
# except Exception as e:
#     print(e.args)
#     print(2)
