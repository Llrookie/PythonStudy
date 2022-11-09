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
print(str1[1:4])  # han
print(str1[0:])  # zhang san  取整个字符串
print(str1[:])  # zhang san  取整个字符串
print(str1[0:-1])  # zhang sa   -1表示最后一位
print(str1[0:-2])  # zhang s    -2表示倒数第二位
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
str5 = 'sfsd'
print(str5.isalnum())  # True

"""
join()
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串
"""

list1 = ['1', '2', '3']
print(''.join(list1))  # 123
print('#'.join(list1))  # 1#2#3

"""
split()函数
语法：str.split(str="",num=string.count(str))[n]
参数说明：
str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
[n]:表示选取第n个分片
返回值：返回一个list列表
"""

str1 = 'zhangsan'
print(str1.split())     # 默认为空格，但不能写成str1.split(''),输出内容：[zhangsan]
print(str1.split('a'))  # ['zh','ngs','n']   将字符串使用指定的字符进行分割为list
print(str1.split('a', 1))  # ['zh','ngsan']  分割一次
print(str1.split('a', 2))  # ['zh', 'ngs', 'n'] 分割两次
print(str1.split('a', 2)[1])   # ngs,分割两次，取第一分片

"""
类型转换
"""
a = 5.5		 # a为float
b = int(a)   # b=5,int类型，不会进行四舍五入

a = 5		   # a为int
b = float(a)   # b=5.0,floatt类型

a = '5'		 # a为string
b = int(a)   # b=5,int类型，只能将纯数字的字符串转换为int类型，不然会报错

a = '1 + 2'
b = eval(a)  # b=3,将字符串的算数表达式计算结果

a = 'zhangsan'
b = dict.fromkeys(a)  # {'z': None, 'h': None, 'a': None, 'n': None, 'g': None, 's': None}
c = dict.fromkeys(a)  # {'z': 10, 'h': 10, 'a': 10, 'n': 10, 'g': 10, 's': 10}

a = 9
print(bin(a))  # 二进制  0b1001
print(oct(a))  # 八进制  0o11
print(hex(a))  # 十六进制  0x9