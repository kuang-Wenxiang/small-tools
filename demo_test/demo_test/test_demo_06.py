
import pytest
import sys

class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_a(self):
        print("------->test_a")
        assert 1

    @pytest.mark.skipif(condition=2 > 1, reason="跳过该函数")  # 跳过测试函数test_b
    def test_b(self):
        print("------->test_b")

    @pytest.mark.xfail(sys.version_info >= (3, 6), reason="Python3.6 API变更")
    def test_function(self):
        assert 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_demo_06.py'])
