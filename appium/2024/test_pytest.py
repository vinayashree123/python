import pytest

# def test_dologin():
#     print('login')
#
# def test_doregister():
#     print('register')

#########################
# @pytest.yield_fixture(scope='module')
# def module_level():
#     print('conn estblish')
#     yield
#     print('disconnect')
#
# @pytest.yield_fixture(scope='function')
# def fun_level():
#     print('open browser')
#     yield
#     print('close browser')
#
# @pytest.mark.usefixtures('module_level','fun_level')
# def test_dologin():
#     print('login')
#
# @pytest.mark.usefixtures('module_level','fun_level')
# def test_doregister():
#     print('register')

# @pytest.yield_fixture(scope='module')
# def module_level():
#     print('conn estblish')
#     yield
#     print('disconnect')
#
# @pytest.yield_fixture(scope='function')
# def fun_level():
#     print('open browser')
#     yield
#     print('close browser')
#
# @pytest.mark.run(order=2)
# def test_dologin():
#     print('login')
#
# @pytest.mark.run(order=1)
# def test_doregister():
#     print('register')

@pytest.mark.flaky()
def test_a():
    a = 1
    b = 2
    assert a == b

