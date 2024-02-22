import pytest

def test_doLogin():
    print("login into the app")

def test_regUser():
    print("registering user")

def test_composeEmail():
    print("composing Email")

#To run single testcase
# pytest .\test_first_testcase.py -s -v -k dologin

#Except this test case run rest all
#  pytest .\test_first_testcase.py -s -v -k "not dologin"

