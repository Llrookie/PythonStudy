# import os
# os.path.dirname(__file__)  获取当前文件所在路径  需要import os
# 方式1：不推荐
# 写
"""f = open('D:\Pytest.txt', 'w')  # 以写（覆盖）的方式打开文件，并得到一个文件对象
f.write('hello world')  # 写入内容
f.close()  # 关闭对象

# 读


f = open('D:\Pytest.txt', 'r')
result = f.read()  # 读文件中所有内容
print(result)
f.close()"""

# 方式2：推荐  读写完成后不用手动关闭对象
# 文件打开模式：r 读，w 覆盖写，a 追加写，b 二进制
# 举例，rb 以二进制读的方式打开文件

# 写
"""with open('D:\Pytest.txt', 'w') as f:
    f.write('python 是最好的语言\n')
    f.writelines(['aaaaa\n', 'bbbbb\n'])  # 写入对象是list类型，但不会自动换行，还需手动加上\n
    # f.close()    #这行写不写都会自动关闭对象
"""
# 读
with open('D:\Pytest.txt', 'r') as f:
    result = f.read()    # 读所有行，以字符串返回
    result1 = f.readline()  # 读第一行，以字符串返回
    result2 = f.readlines()   # 读所有行，以列表形式返回，每行作为一个元素，后面会自动带上\n ['python 是最好的语言\n', 'aaaaa\n', 'bbbbb\n']
    result3 = f.read().splitlines()  # 读所有行，以列表形式返回，每行作为一个元素，后面会自动取掉\n ['python 是最好的语言', 'aaaaa', 'bbbbb']
    print(result3)

# 有多个读取方法时，后面的读取内容以前一个方法读取之后剩下的内容为基准
# eg1:
# result = f.read()    这里读取了所有内容
# result = f.readline()  以上面读取之后剩下的内容为基准，那这里读到的内容就是空的

# eg2:
# result = f.readline()    这里读取了第一行
# result = f.readlines()    以上面读取之后剩下的内容为基准，读取除第一行以外的数据

