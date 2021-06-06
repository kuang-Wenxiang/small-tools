

import  pytest

class Test_comm():

    @pytest.mark.run(order=2)
    def test_fun1(self):
        print(1)

    @pytest.mark.run(order=1)
    def test_fun2(self):
        assert 2<1