import os
"""生成多层递归目录"""
# os.makedirs('dir1/dir2')
"""若目录为空，则删除，并递归到上一级目录，若也为空则删除，以此类推"""
# os.removedirs('dir1')
# os.mkdir('dir3/dir4')
"""删除单级空目录，若目录不为空则无法删除：报错，相当于shell中的rmdir dirname"""
# os.rmdir('dir3/dir4')
"""列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表的方式打印"""
# path = 'C:/Users\Administrator\gitPH\small-tools\demo_test\常用模块'
# print(os.listdir(path))
"""删除一个文件"""
# os.remove()
"""重命名文件/目录"""
# os.rename("oldname", "newname")
"""获取文件/目录信息"""
# os.stat('path/filename')
"""运行shell命令，直接显示"""
# os.system("bash command")
"""运行shell命令，获取执行结果"""
# os.popen("bash command").read()
"""获取当前的工作目录，即当前的python脚本工作的目录路径"""
# print(os.getcwd())
"""改变当前脚本工作目录，相当于shell下cd"""
# os.chdir("dirname")

"""os.path"""
"""返回path规范化的绝对路径，os.path.split(path)将path分割成目录和文件名二元组返回"""
# print(os.path.abspath('path'))
"""返回path的目录，其实就是os.path.split(path)的第一个元素"""
# os.path.dirname('path')
"""返回path最后的文件名，如何path以/或\结尾，那么就会返回空值，即os.path.split(path)的第二个元素"""
# os.path.basename('path')
"""第二个元素"""
"""如果path存在，返回true，如果不存在，返回false"""
# os.path.abspath('path')
"""如果path是绝对路径，返回false"""
# os.path.isabs('path')
"""如果path是一个存在的文件，返回true，否则返回false"""
# os.path.isfile('path')
"""如果path是一个存在的目录，返回true，否则返回false"""
# os.path.isdir('path')
"""将多个路径组合后返回，第一个绝对路径之前的参数将被忽略"""
# os.path.join('path', [path])
"""返回path所指向的文件或目录的最后访问时间"""
# os.path.getatime('path')
"""返回path所指向的文件或目录的最后修改时间"""
# os.path.getmtime('path')

"""返回path的大小"""
# os.path.getsize('path')

"""EG"""
# usr = input("输入用户名：")
# password = input("输入密码：")
# if usr=="usr"and password=="password":
#     os.makedirs('%s'%(usr))






















