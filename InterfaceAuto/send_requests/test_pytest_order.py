import pytest


class TestOrdering():
    age = 18

    @pytest.mark.run(order=3)
    def test_order_01(self):
        print('这是第一个测试方法')

    @pytest.mark.run(order=2)
    def test_order_02(self):
        print('这是第二个测试方法')

    @pytest.mark.run(order=1)
    def test_order_03(self):
        print('这是第三个测试方法')


if __name__ == '__main__':
    pytest.main()
