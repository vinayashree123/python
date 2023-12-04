import requests

# url = 'http://httpbin.org/#/Auth/get_basic_auth__user___passwd_'
# auth_res = requests.get(url,auth=('us','passw'))
# print(auth_res.status_code)
# if auth_res.status_code == 200:
#     print('Sucessful authentication.')
# else:
#     print('Unsuccessful authentication.')


#
# #exam2
url = 'http://httpbin.org/#/Auth/get_digest_auth__qop___user___passwd___algorithm___stale_after_'
auth_res = requests.get(url,auth=('user','passwd'),params={'qop':'auth','algorithm':'MD5','stale_after':'neve'},)
print(auth_res.status_code)
