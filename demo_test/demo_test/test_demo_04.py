import pytest


@pytest.fixture()
def test1():
    a = 'door'
    b = '123456'
    print('传出a,b')
    return (a, b)


def test_2(test1):
    u = test1[0]
    p = test1[1]
    assert u == 'door'
    assert p == '123456'
    print('元祖形式正确')


if __name__ == '__main__':
    pytest.main(['-s', 'test_abc.py'])
