import requests

se = requests.session()
se.auth = auth=('user','passwd')
url = 'http://httpbin.org/#/Auth/get_basic_auth__user___passwd_'
res = se.get(url)
print(res.status_code)


#Example2
se = requests.session()
se.cookies.update({'visit-month':'February'})

res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2022'})
print(res.text)

# res = se.get("https://httpbin.org/cookies",cookies={'visit-day':'monday'})
# print(res.text)
