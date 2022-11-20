import pytest


@pytest.fixture(scope="function")
def connect_sql():
    print('连接数据库')
    yield
    print('关闭数据库')