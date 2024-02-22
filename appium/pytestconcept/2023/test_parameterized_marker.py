 # pytest .\test_user_defined_marker.py -v -s -m "not functional"

import pytest
def getData():
    return [
        ('vina','vina@123'),
        ('rama','rama@123')
    ]

@pytest.mark.parametrize("username,password",getData())
def test_userlogin(username,password):
    print(username, '___' ,password)
