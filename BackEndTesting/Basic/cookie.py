import requests

# url = 'http://httpbin.org/#/Cookies/get_cookies'
# cookie = {'visit_year' : '2023'}
# res = requests.get(url,cookies=cookie)
# print(res.status_code)
# if res.status_code == 200:
#     print('Request was successful')
#     # Access and print the value of a specific cookie
#     specific_cookie_value = res.cookies.get('visit_year')
#     print('Value of cookie_name1:', specific_cookie_value)
# else:
#     print('Request failed with status code:', res.status_code)
#
url='http://httpbin.org/#/Cookies/get_cookies_set__name___value_'
cookie = {'name' : 'vina','value' : '122'}
res = requests.get(url,cookies=cookie)
print(res.status_code)

# response = requests.get('http://example.com')
# cookies = response.cookies
# print(cookies.get_dict())
# response2 = requests.get('http://example.com', cookies=cookies)

