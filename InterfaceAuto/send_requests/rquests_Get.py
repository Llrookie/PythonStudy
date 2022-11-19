import requests

url = 'https://api.weixin.qq.com/cgi-bin/token'
data = {
    "grant_type": "client_credential",
    "appid": "wx6b11b3efd1cdc290",
    "secret": "106a9c6157c4db5f6029918738f9529d"
}
rep = requests.get(url=url, params=data)
# 如果数据格式要求为json
# res = requests.post(url=url, json=data)
print(rep.text)
print(rep.json()['access_token'])
print(rep.status_code)

# 解析响应结果
print(rep.text)
# 断言，校验预期结果和实际结果
reason = 'successed'
# rep.json()['reason'] 通过key获取对应的value值
assert reason == rep.json()['access_token'], "断言失败"
