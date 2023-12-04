# In this file we need to add after_scenario & before_scenario
# after_scenario - it will execute after each scenario
# before_scenario - it will execute before each scenario


import requests

def after_scenario(context,scenario):
    response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": context.bookId
}, headers={"Content-Type": "application/json"},
                                    )
    #validation
    assert  response_deleteBook.status_code == 200
    res_json = response_deleteBook.json()
    print(res_json['msg'])

