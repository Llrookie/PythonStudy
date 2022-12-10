import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from InterfaceAuto.emails.email_Manage import emailMange


class TestEmailSend(unittest.TestCase):
    def test_01_case(self):
        print('案例1')

    def test_02_case(self):
        print('案例2')

    def test_03_case(self):
        print('案例3')


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./', '*.py')
    files = open('./report.html', 'wb')
    runner = HTMLTestRunner(stream=files, title='邮件发送学习报告', description='文件描述')
    runner.run(suite)
    files.close()  # 一定要关闭文件流
    time.sleep(4)
    emailMange().email_send(files.name)
