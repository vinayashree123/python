import pytest


# two ways we have module and function level

@pytest.fixture(scope='function')
def setup():
    print("Launch browser")
    yield
    print("close browser")

#module level
# def setup_module(module):
#     print("connecting DB connection")
#
# def teardown_module(module):
#     print("close DB connection")

@pytest.fixture(scope='module')
def module_level():
    print("connecting DB connection")
    yield
    print("close DB connection")


# def test_doLogin(setup,module_level):
#     print("login into the app")
#
# def test_regUser(setup,module_level):
#     print("registering user")

@pytest.mark.usefixtures('setup','module_level')
def test_doLogin():
    print("login into the app")

@pytest.mark.usefixtures('setup','module_level')
def test_regUser():
    print("registering user")
