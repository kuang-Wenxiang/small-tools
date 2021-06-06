"""
简单灵活，容易上手
支持参数化
能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appium等自动化测试，接口自动化测试（pytest+request）

pytest具有很多第三方插件，并且可以自定义扩展，比较好用的如pytest-selenium（集成selenium）、pytest-html（完美html测试报告生成）、
pytest-rerunfailures（失败case重复执行）、pytest-xdist（多CPU分发）等

测试用例的skip和xfail处理
可以很好的和Jenkins集成
"""

"""
pytest.main(["-s","test_abc.py"])

通过python代码执行 pytest.main()
1.直接执行pytest.main() 【自动查找当前目录下，以test_开头的文件或者以_test结尾的py文件】
2.设置pytest的执行参数 pytest.main(['--html=./report.html','test_login.py'])【执行test_login.py文件，并生成html格式的报告】
main()括号内可传入执行参数和插件参数，通过[]进行分割，[]内的多个参数通过‘逗号,’进行分割
运行目录及子包下的所有用例  pytest.main(['目录名'])
运行指定模块所有用例  pytest.main(['test_reg.py'])
运行指定模块指定类指定用例  pytest.main(['test_reg.py::TestClass::test_method'])  冒号分割
 
-n=xxx: 多并发
-m=xxx: 运行打标签的用例
-reruns=xxx，失败重新运行
-q: 安静模式, 不输出环境信息
-v: 丰富信息模式, 输出更详细的用例执行信息
-s: 显示程序中的print/logging输出
--resultlog=./log.txt 生成log
--junitxml=./log.xml 生成xml报告
--html=report.html 生成HTML文件
"""

"""
Pytest Exit Code 含义清单

Exit code 0 所有用例执行完毕，全部通过
Exit code 1 所有用例执行完毕，存在Failed的测试用例
Exit code 2 用户中断了测试的执行
Exit code 3 测试执行过程发生了内部错误
Exit code 4 pytest 命令行使用错误
Exit code 5 未采集到可用测试用例文件
"""

"""
Pytest的setup和teardown函数
1.setup和teardown主要分为：模块级,类级，功能级，函数级。
2.存在于测试类内部

函数级别setup()／teardown()

运行于测试方法的始末，即:运行一次测试函数会运行一次setup和teardown
"""

"""
方法：fixture(scope="function", params=None, autouse=False, ids=None, name=None)
常用参数:
scope：被标记方法的作用域  session>module>class>function
function" (default)：作用于每个测试方法，每个test都运行一次
"class"：作用于整个类，每个class的所有test只运行一次 一个类中可以有多个方法
"module"：作用于整个模块，每个module的所有test只运行一次；每一个.py文件调用一次，该文件内又有多个function和class
"session：作用于整个session(慎用)，每个session只运行一次；是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
params：(list类型)提供参数数据，供调用标记方法的函数使用；一个可选的参数列表，它将导致多个参数调用fixture功能和所有测试使用它。
autouse：是否自动运行,默认为False不运行，设置为True自动运行；如果True，则为所有测试激活fixture func可以看到它。如果为False则显示需要参考来激活fixture<br><br>ids：每个字符串id的列表，每个字符串对应于params这样他们就是测试ID的一部分。如果没有提供ID它们将从params自动生成;是给每一项params参数设置自定义名称用，意义不大。
"""
"""
1. fixture 可以作为一个函数的参数被调用
2. fixture可以在一个类、或者一个模块、或者整个session中被共享，加上范围即可

"""