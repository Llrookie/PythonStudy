import requests
# 需安装pytest  pip install pytest

class TestGetrequests:
    def test_getrequests(self):
        url = 'http://v.juhe.cn/laohuangli/d'
        data = {
            "key": "82aecd06c3d7f59f572c7fa57cc1ca85",
            "date": "2022-03-01"
        }

        rep = requests.get(url=url, params=data)
        print(rep.json())


if __name__ == '__main__':
    pytest.main([-vs])
