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
