import requests

url = 'http://rahulshettyacademy.com'
cookie = {'visit-month':'February'}
response = requests.get(url,allow_redirects=False,cookies=cookie,timeout=1)
#301,200
# print(response.history)
print(response.status_code)

#Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('imagecomparasion.png', 'rb')}
r= requests.post(url,files=files)
# print(r.status_code)
print(r.text)
