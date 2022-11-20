import requests
import pytest
from InterfaceAuto.common.yaml_unit import YamlUnit


class TestRelationrequests:

    """
    # 也可以单独写在这里，也可以写在conftest.py文件里
    @pytest.fixture(scope="function")
    def connect_sql():
        print('连接数据库')
        yield
        print('关闭数据库')
    """

    # 不再使用类全局变量是进行上下接口关联，通过读取yaml文件操作

    # get请求
    # connect_sql是使用该函数前，手动调用前置函数，不用导入，直接使用
    def test_get_Token(self,connect_sql):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }

        rep = requests.request('get', url=url, params=data)
        print('test_getToken is ok')
        # 将access_token参数写入文件

        YamlUnit().write_extract_yaml({"access_token": rep.json()['access_token']})


    # post请求
    def test_edit_flag(self):
        # 将需要的数据读出来
        value = YamlUnit.read_extract_yaml('access_token')

        url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token=' + value + ""
        data = {
            "tag": {"id": 134, "name": "广东人"}
        }

        rep = requests.request('post', url=url, json=data)
        print(rep.json())
        print('test_edit_flag is ok')


if __name__ == '__main__':
    pytest.main()
