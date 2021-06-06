
import pytest
import time
import random


class TestWayangCommon:

    def setup(self):
        print("获取用户登录信息")

    def teardown(self):
        print("防止跟踪")

    def teardown_class(self):
        print("退出")

    def setup_class(self):
        print("登录")

    def before(self):
        print("///////")

    @pytest.mark.run(order=2)
    def test_demo_01(self):
        print("逛首页")

    @pytest.mark.skipif(condition=1>2, reason="参数condition为False,不跳过测试")  # 参数condition为True,跳过测试
    def test_demo_02(self):
        print("买东西")

    @pytest.mark.skip()
    def test_demo_03(self):
        print("不买东西")

    def test_demo_04(self):
        assert 1 != 1

    @pytest.fixture(autouse=True)
    def test_demo_05(self):
        # return 2
        print("///////")
    def test_demo_06(self, test_demo_05):
        print(test_demo_05)

    @pytest.fixture(scope="module")
    # @pytest.fixture(scope="class")
    # @pytest.fixture(scope="session")
    def test_demo_07(self):
        pass

    def test_demo_09(self, params):
        print("//////")

    @pytest.mark.parametrize("a,b", [(1, 2), (2, 3)])
    def test_demo_110(self, a, b):
        print(a, b)





@pytest.fixture(scope="module", params=["case1", "case2", "case3"])
def params(request):
    return request.param


