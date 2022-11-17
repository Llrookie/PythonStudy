import requests

url = 'http://v.juhe.cn/jztk/query'
data = {
    "subject": "1",
    "model": "c1",
    "key": "674322ee5b01b89cfd767764479e0536",
    "testType": "rand"
}
rep = requests.post(url=url, json=data)
print(rep.json())
