import pytest


class TestSkip():
    age = 18

    @pytest.mark.skip('无理由跳过')
    def test_skip_01(self):
        print('这是第一个测试方法')

    @pytest.mark.skipif(age >= 10, reason='大于10就跳过')
    def test_skip_02(self):
        print('这是第二个测试方法')

    def test_skip_03(self):
        print('这是第三个测试方法')


if __name__ == '__main__':
    pytest.main()
