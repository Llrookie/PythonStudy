import re
import requests

# 需安装pytest  pip install pytest

"""
    1、使用session来替代cookie鉴权
    2、统一请求方式，使用request.request('get/post',url=url,data=data)
"""


class TestGetrequests:
    # 类变量，通过类名.变量访问
    access_token = ''
    csrf_token = ''
    # session，会话，让多个请求在同一会话内，cookie等可共享
    session = requests.session()

    # get请求
    def test_get_Token(self):
        url = 'https://api.weixin.qq.com/cgi-bin/token'
        data = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }

        rep = requests.request('get', url=url, params=data)
        TestGetrequests.access_token = rep.json()['access_token']
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

    # 正则表达式获取值
    def test_start(self):
        url = 'https://47.107.116.139/phpwind'

        rep = TestGetrequests.session.request('get', url=url)
        print(rep.text)
        """re.search('a',b)可以使用正则表达式获取
        a:想获取内容的左右值，将想获取的内容改成(.*?)   
        re.search('host='(.*?)', port=443')   即想从host='47.107.116.139', port=443里获取ip地址
        b.内容部分，及rep.text"""
        # 表示取第一个值
        TestGetrequests.csrf_token = re.search("host='(.*?)', port=443", rep.text)[1]
        TestGetrequests.cks = rep.cookies

    # 需要带请求头的接口以及需要cookie关联的接口
    def test_login(self):
        url = 'https://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
        data = {
            "age": 10,
            "name": "Tom",
            "sex": "Man"
        }

        headers = {
            "Accept": "application/json, text/javascript, /; q = 0.01",
            "X-Requested-With": "XMLHttpRequest"
        }

        rep = TestGetrequests.session.request('post', url=url, json=data, headers=headers)
        print(rep.json())


if __name__ == '__main__':
    pytest.main([-vs])
