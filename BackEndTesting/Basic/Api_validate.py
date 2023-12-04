import requests

# url = 'http://216.10.245.166/Library/GetBook.php'
res = requests.get('http://216.10.245.166/Library/GetBook.php',params={'AuthorName':'Rahul Shetty'})
print(res.json())
json_res = res.json()
print(type(json_res))
assert json_res[0]['book_name'] == 'Postman Cours'
# print(res.status_code)
# print(res.headers)

# Retrieve the book details with ISBN MWA22
for book in res.json():
    # print(book)
    if book['isbn'] == 'MWA22':
        print(book)






