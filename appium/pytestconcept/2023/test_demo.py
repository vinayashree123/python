import pytest


@pytest.fixture(scope='function')
def function_level():
    print('open browser')
    yield
    print('close browser')


@pytest.fixture(scope='module')
def module_level():
    print('estblish db connection')
    yield
    print('close connection')


@pytest.mark.usefixtures('module_level','function_level')
def test_dologin():
    print('login to website')


@pytest.mark.usefixtures('module_level','function_level')
def test_reguser():
    print('registering user')
