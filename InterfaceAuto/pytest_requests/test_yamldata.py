import requests
import pytest
from InterfaceAuto.common.yaml_unit import YamlUnit


class TestRelationrequests:

    # 不再使用类全局变量是进行上下接口关联，通过读取yaml文件操作

    # get请求
    # connect_sql是使用该函数前，手动调用前置函数，不用导入，直接使用
    @pytest.mark.parametrize('caseinfo',YamlUnit().read_get_token_yaml())
    def test_get_Token(self,caseinfo):
        url = caseinfo['requests']['url']
        data = caseinfo['requests']['data']
        method = caseinfo['requests']['method']

        rep = requests.request(method, url=url, params=data)
        print('test_getToken is ok')
        # 将access_token参数写入文件

        YamlUnit().write_extract_yaml({"access_token": rep.json()['access_token']})


if __name__ == '__main__':
    pytest.main(['test_yamldata.py'])
