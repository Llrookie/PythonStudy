import pytest

from InterfaceAuto.common.yaml_unit import YamlUnit


@pytest.fixture(scope="function")
def connect_sql():
    print('连接数据库')
    yield
    print('关闭数据库')

# 前置清楚yaml文件
@pytest.fixture(scope='session',autouse=True)
def clear_yaml():
    YamlUnit().clear_extract_yaml()