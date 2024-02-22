import pytest
@pytest.yield_fixture(scope='module')
def Beforeclass():
    print("this is before class")
    yield
    print("after class")
@pytest.yield_fixture()
def Before_Method():
    print("this is before Method")
    yield
    print("after method")

def test_MethodA(Before_Method,Beforeclass):
    print("this is method A")

def test_MethodB(Before_Method,Beforeclass):
    print("this is method B")

# @pytest.fixture()
# def After_Method():
#     print("this is before Method")
#
# def test_MethodA(Before_Method):
#     print("this is method A")
#
# def test_MethodB(Before_Method):
#     print("this is method B")

