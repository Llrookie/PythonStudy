import requests

url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token=62_aUg9SRpMOfD2uDsnSJQd9Th5pX1__MqS4mNTEU1BtyK3H-EAnt40HN4GnGUA73BaNNekbuk26Xt3eHvNTRqSz9hW7oVBc6WFzcCkk8ZFmKdzbBzMcR249LB1PkEESChAGASGQ'
data = {
    "tag": {"id": 134, "name": "广东人"}
}

rep = requests.post(url=url, json=data)
print(rep.json())

class file_upload:
    def test_file_upload(self):
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=62_nPNqDS_NXIi-xa_CRY44ZQ_Heknlxx_8-T4whr8mGje1LxLuaWPVVQFUyRLTURAwt37ZUVpWtB2G9xDrS_oB8jQqbApKuEDe-VRBGsij0konUPCKHaQClfwnwL4VFXiAAANXP'
        data = {
            "media": open(r"C:\Users\King\Pictures\壁纸\86839.jpg", 'rb')
        }
        # 上传文件需用open()打开文件，以rb二进制，并且是files格式
        rep = requests.post(url=url, files=data)
        print(rep.json())

if __name__ == '__main__':
    filetest = file_upload()
    filetest.test_file_upload()