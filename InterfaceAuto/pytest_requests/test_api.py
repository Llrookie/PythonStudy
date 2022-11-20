import pytest

"""
    yaml数据传参测试
"""

class Testapi():
    @pytest.mark.parametrize("args", ['kangkang', 'jiating'])
    def test_api1(self, args):
        print(args)

    @pytest.mark.parametrize('name,age', [['百里', 12], ['康康', 19]])
    def test_api2(self, name, age):
        print(name, age)

    @pytest.mark.parametrize('args', [['百里', 12], ['康康', 19]])
    def test_api3(self, args):
        print(args)


if __name__ == '__main__':
    pytest.main(['test_api.py'])
