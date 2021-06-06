import pytest


@pytest.fixture()
def test1():
    print('\n开始执行function')


@pytest.mark.usefixtures('test1')
def test_a():
    print('---用例a执行---')


@pytest.mark.usefixtures('test1')
class Test_Case:
    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')


if __name__ == '__main__':
    pytest.main(['-s', 'test_demo_05.py'])

# import pytest
#
#
# @pytest.fixture(params=[1, 2, 3])
# def need_data(request):  # 传入参数request 系统封装参数
#     return request.param  # 取列表中单个值，默认的取值方式
#
#
# class Test_ABC:
#     def test_a(self, need_data):
#         print("------->test_a")
#         assert need_data != 3  # 断言need_data不等于3
#
#
# if __name__ == '__main__':
#     pytest.main(["-s", "test_demo_05.py"])
