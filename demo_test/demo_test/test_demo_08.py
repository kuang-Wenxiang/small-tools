# content of test_server.py

# import pytest
#
#
# @pytest.mark.webtest
# def test_send_http():
#     pass  # perform some webtest test for your app
#
# @pytest.mark.webtest
# def test_something_quick():
#     pass
#
#
# def test_another():
#     pass
#
#
# class TestClass:
#     def test_method(self):
#         pass


import pytest

seq = ["case1", "case2", "case3"]


@pytest.fixture(scope="module", params=seq)
def params(request):
    return request.param


def test_params(params):
    print(params)
    assert "case" in params
