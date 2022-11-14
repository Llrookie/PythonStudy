# 方式1  DOM:文件对象模型(document object model) 不推荐
# 方式2  elementTree
import xml.etree.ElementTree as ET  # 导入包并重命名为ET


def xml_read(file_name, node_name):
    datas = []  # 定义一个空列表，用来存放数据
    tree = ET.parse(file_name)  # 得到树
    root = tree.getroot()  # 得到根节点
    for i in root.iter(node_name):  # 循环变量指定的所有节点
        datas.append(i.text)  # 将匹配的节点加入到列表
    return datas


if __name__ == '__main__':
    result = xml_read('1.xml', 'username')
    print(result)  # ['admin', 'admin123']  多个都可以读取到，包括子节点
