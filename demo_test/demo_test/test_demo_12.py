
import pytest


class TestComm():

    def setup(self):
        print("获取用户登录信息")
    @pytest.fixture()
    def fun(self):
        print("获取用户登录信息")

    @pytest.mark.usefixtures('fun')
    def test_fun1(self):
        print(1)

    def test_fun2(self):
        print(2)

    def test_fun3(self):
        print(3)

