import requests
import pytest

@pytest.fixture(scope='function')
def fixfunction():
    print('这是前置方法')

class TestGetrequests:

    # 前置
    def setup(self):
        print('在每个用例执行前执行')

    # 后置
    def teardown(self):
        print('在每个用例执行后执行')

    # 类变量，通过类名.变量访问
    access_token = ''
    csrf_token = ''
    # session，会话，让多个请求在同一会话内，cookie等可共享
    session = requests.session()

    # get请求

    def test_get_Token(self, fixfunction):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }

        rep = requests.request('get', url=url, params=data)
        print('test_getToken is ok')

    # post请求
    def test_edit_flag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token=' + TestGetrequests.access_token + ""
        data = {
            "tag": {"id": 134, "name": "广东人"}
        }

        rep = requests.request('post', url=url, json=data)
        print(rep.json())
        print('test_edit_flag is ok')

    # 文件上传接口
    def test_file_upload(self):
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=' + TestGetrequests.access_token + ""
        data = {
            "media": open(r"C:\Users\King\Pictures\壁纸\86839.jpg", 'rb')
        }
        # 上传文件需用open()打开文件，以rb二进制，并且是files格式
        rep = requests.request('post', url=url, files=data)
        print(rep.json())
        print("test_file_upload is ok")


if __name__ == '__main__':
    pytest.main()
