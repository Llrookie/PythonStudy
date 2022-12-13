import os
import yaml


class YamlUnit:
    # 读取yaml文件
    def read_extract_yaml(self,key):
        with open('K:\PythonProject\PythonStudy\extract.yml', 'r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]


    # 写入yaml文件
    def write_extract_yaml(self, data):
        with open('K:\PythonProject\PythonStudy\extract.yml', 'a', encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清除yaml文件，每次会追加写入的内容，导致过多
    # 此方法可以写入前置方法里，自动执行
    def clear_extract_yaml(self):
        with open('K:\PythonProject\PythonStudy\extract.yml', 'w', encoding='utf-8') as f:
            f.truncate()

    # 读取测试用例的yaml文件
    def read_get_token_yaml(self):
        with open('K:\PythonProject\PythonStudy\get_token.yml', 'r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
