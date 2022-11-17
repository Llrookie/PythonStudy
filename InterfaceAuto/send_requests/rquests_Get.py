import requests

url = 'http://v.juhe.cn/laohuangli/d'
data = {
    "key": "82aecd06c3d7f59f572c7fa57cc1ca85",
    "date": "2022-03-01"
}
rep = requests.get(url=url, params=data)
# 如果数据格式要求为json
# res = requests.post(url=url, json=data)
print(rep.text)
print(rep.json())
print(rep.status_code)

# 解析响应结果
print(rep.text)
# 断言，校验预期结果和实际结果
reason = 'successed'
# rep.json()['reason'] 通过key获取对应的value值
assert reason == rep.json()['reason'], "断言失败"