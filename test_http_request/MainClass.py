import traceback
import requests

print('## 开始')
token = ''

title = '登录接口'
print('\n## {} START !'.format(title))
try:
    url2 = 'http://localhost:8090/auth/login?name=zhangyunfei&password=vir56k'
    r = requests.get(url2)
    print(r.text)
    j = r.json()
    token = j['data']['token'];
    print('token='+token)
    assert token != ''
except Exception as e:
    print(e)
    raise RuntimeError(e)
finally:
    print('## {} DONE !'.format(title))

title = '验证 跳过token声明的 passtoken'
print('\n## {} START !'.format(title))
try:
    url = 'http://localhost:8090/auth/test'
    r = requests.get(url)
    print(r.text)
    res = r.text
    assert res != ''
except Exception as e:
    print(e)
    raise RuntimeError(e)
finally:
    print('## {} DONE !'.format(title))

title = '验证 无token 时返回500'
print('\n## {} START !'.format(title))
try:
    url = 'http://localhost:8090/channel/test'
    r = requests.get(url)
    print(r.text)
    res = r.json()
    assert res['code'] != 200
except Exception as e:
    print(e)
    raise RuntimeError(e)
finally:
    print('## {} DONE !'.format(title))

title = '验证 有token 时 200'
print('\n ## {} START !'.format(title))
try:
    url = 'http://localhost:8090/channel/test'
    header = {'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhdXRoMCIsImV4cCI6MTU3MDc2NTY5MSwiaWF0IjoxNTcwNzIyNDkxLCJqdGkiOiJ6aGFuZ3l1bmZlaSJ9.f4X9caBpyd2RbdLScR-qc1jo7kN39E6UgDf-eadm9aA'}
    r = requests.get(url,headers=header)
    print(r.text)
    res = r.json()
    assert res['code'] == 200
except Exception as e:
    print(e)
    raise RuntimeError(e)
finally:
    print('## {} DONE !'.format(title))

title = 'xxxx'
print('\n ## {} START !'.format(title))
try:
    url = 'http://localhost:8090/channel/list'
    header = {'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhdXRoMCIsImV4cCI6MTU3MDc2NTY5MSwiaWF0IjoxNTcwNzIyNDkxLCJqdGkiOiJ6aGFuZ3l1bmZlaSJ9.f4X9caBpyd2RbdLScR-qc1jo7kN39E6UgDf-eadm9aA'}
    r = requests.get(url,headers=header)
    print(r.text)
    res = r.json()
    assert res['code'] == 200
except Exception as e:
    print(e)
    raise RuntimeError(e)
finally:
    print('## {} DONE !'.format(title))



