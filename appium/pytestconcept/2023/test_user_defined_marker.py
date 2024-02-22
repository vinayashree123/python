import pytest

@pytest.mark.functional
def test_doLogin():
    print("login into the app")

@pytest.mark.regression
def test_regUser():
    print("registering user")

@pytest.mark.functional
def test_composeEmail():
    print("composing Email")


#Run
# pytest .\test_user_defined_marker.py -v -s -m functional

#Except Functional
# pytest .\test_user_defined_marker.py -v -s -m "not functional"

