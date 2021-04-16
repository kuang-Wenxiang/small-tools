"""
执行一个文件夹中的所有的py文件
"""
# import os
#
#
# def func(path):
#     if os.path.isfile(path):
#         if path.endwith('.py'):
#             os.system('python %s' % path)
#     elif os.path.isdir(path):
#         for name in os.listdir(path):
#             path_abs = os.path.join(path, name)
#             if path_abs.endswith('.py'):
#                 os.system('python %s' % path_abs)
#
#
# func('C:/Users\Administrator\gitPH\small-tools\demo_test\常用模块')


"""
移动一个文件
"""
# import os
#
#
# def func(path1, path2):
#     """path1:原文件的位置"""
#     """path2:目标位置"""
#     file_name = os.path.basename(path1)
#     print(file_name)
#     with open(path1, 'rb') as f1, open(os.path.join(path2, file_name), 'wb') as f2:
#         content = f1.read()
#         f2.write(content)
#
#
# func(r'C:\Users\Administrator\gitPH\small-tools\demo_test\常用模块\test.py',
#      r'C:\Users\Administrator\gitPH\small-tools\demo_test\练习题')

"""文件的上一级目录"""
# import os
# def func(path):
#     path1 = os.path.dirname(path)
#     path2 = os.path.dirname(path1)
#     print(path2)
#
#
# func(r'C:\Users\Administrator\gitPH\small-tools\demo_test\练习题\demo_文件操作.py')

"""文件信息登录"""
# import os
# import pickle
# import json
#
#
# def register():
#     usr = input("username:")
#     password = input("password:")
#     dic = {usr: password}
#     with open('userinfo', 'ab') as f:
#         pickle.dump(dic, f)
#     print("注册成功！")
#
#
# def login():
#     flag = True
#     usr = input("username:")
#     password = input("password:")
#     with open('userinfo', 'rb') as f:
#         while flag:
#             try:
#                 dic = pickle.load(f)
#                 for k, v in dic.items():
#                     if k == usr and password == v:
#                         print("登录成功！")
#                         flag = False
#                         break
#             except EOFError:
#                 print("登录失败！")
#                 break
#
# register()
# login()


"""发红包：random"""
