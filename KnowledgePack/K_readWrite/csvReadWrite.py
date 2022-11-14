# 文件，逗号分隔符，纯文本文件，通常用来存储测试数据
import csv

# 写
# newline=''解决每次多写入一个空行
# encoding='utf8' 解决乱码
with open('2.csv', 'a', newline='', encoding='utf8') as f:
    obj = csv.writer(f)  # 得到一个写CSV文件的对象
    obj.writerow(['5', '中国人', '16'])  # 向csv文件写入一行数据

# 读
with open('2.csv', 'r', encoding='utf8') as f:
    obj = csv.reader(f)
    for i in obj:
        print(i)
