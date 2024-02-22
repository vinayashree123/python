import pytest


# two ways we have module and function level

def setup_function(function):
    print("Launch browser")


def teardown_function(function):
    print("close browser")


# module level
def setup_module(module):
    print("connecting DB connection")


def teardown_module(module):
    print("close DB connection")


def test_doLogin():
    print("login into the app")


def test_regUser():
    print("registering user")


#

