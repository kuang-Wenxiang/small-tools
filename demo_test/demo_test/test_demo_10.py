
import unittest


class uini(unittest.TestCase):

    def setUp(self):
        print("//01")

    # def setUpClass(self):
    #     print("////////01")

    def tearDown(self) -> None:
        print("/////0004")

    def test_demo_01(self):
        print("////03")
        assert 2<1

    def test_demo_02(self):
        print("////04")
        self.assertCountEqual(1, 1)
