import requests

url = 'http://216.10.245.166//Library/Addbook.php'
headers = {"Content-Type": "application/json"}
addbook_res = requests.post(url,json={
"name": "Learn Appium Automation with Java",
"isbn": 'V10',
"aisle": "227",
        "author": "John foe"},headers=headers)
print(addbook_res.json())
res_json = addbook_res.json()

#validation
if res_json['Msg'] != 'Book Already Exists':
        assert res_json['Msg'] == 'successfully added'

# delete book
bookId = res_json['ID']
print(bookId)
url = 'http://216.10.245.166//Library/DeleteBook.php'
deletebook_res = requests.post(url,json={'ID':bookId})
print(deletebook_res.json())
#
#
# #validation
# res_json = deletebook_res.json()
# assert res_json['msg'] == 'book is successfully deleted'
