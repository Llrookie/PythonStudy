"""# 变量分为数字型和非数字型
# 数字型：整型(int)、浮点型(float)、布尔型(bool)、复数型(complex)
# 支持int，float，bool(布尔值)，complex(复数)
    # python3中只有一种整数类型int，表示为长整型
    # 内置的type(）可以查看变量对应的对象类型
    # 内置的id()函数可以查看变量的内存空间地址
    # 数值的除法( /)总是返回一个浮点数，取整用 //，取余用 %
    # 在混合运算时，python会把整型转化为浮点数

# 非数字型：字符串、列表、元组、字典"""

a = 1  # 整型int
b = 1.0  # 浮点型float
print(5 / 2)  # 2.5 除
print(5 // 2)  # 2  取整
print(5 % 2)  # 1  取余
print(type(a))

""" python中变量不需要申明，每个变量在使用前必须赋值，赋值之后该变量才会被创建
    python中允许同时为多个变量赋值
"""

# 输出结果a,b,c都为1
a = b = c = 1
print(a, b, c)

"""string 字符串
    内容由''或者""括起来的内容
    字符串中可以用\来转义
        转义符: \n  回车,\t   制表符tab,\r  换行,\\代表一个反斜杠
    字符串和数值不能使用+拼接
"""
str1 = 'zhang san'
str2 = "li si"
# 切片，左闭右开
print(str1[0:4])  # zhan
# print(str1[1:4])  #han
print(str1[0:])  # zhang san  取整个字符串
print(str1[:])  # zhang san  取整个字符串
print(str1[0:-1])  # zhang sa   -1表示最后一位
print(str1[0:9:2])  # zagsn 2表示步长，从第一位开始，然后取第三位、第五位...
# 转义
str3 = 'zhang\nsan'
str4 = r'zhang\nsan'
print(str3)  # zhang  san打印在两行
print(str4)  # zhang\nsan   在字符串前面加r或R，字符串原样输出
# *复制显示
str1 = 'hello'
print(str1 * 2)  # hellohello

"""字符串内置方法
isdigit():判断字符串是否为纯数字
isalpha():判断字符串是否为纯字母
isupper():判断字符串是否为纯大写
islower():判断字符串是否为纯小写
isalnum():判断字符串是否为字母或数字
join(list):可以将列表转成string，列表中元素必须为字符串
split():将字符串分割
"""
# join()
list1 = ['1', '2', '3']
print(''.join(list1))  # 123
print('#'.join(list1))  # 1#2#3

# split()
str1 = 'zhangsan'
print(str1.split('a'))  # ['zh','ngs','n']   将字符串使用指定的字符进行分割为list
print(str1.split('a'), 1)  # ['zh','ngsan']  分割一次
