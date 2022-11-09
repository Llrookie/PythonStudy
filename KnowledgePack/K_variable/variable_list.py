"""# 变量分为数字型和非数字型
# 数字型：整型(int)、浮点型(float)、布尔型(bool)、复数型(complex)
# 支持int，float，bool(布尔值)，complex(复数)
    # python3中只有一种整数类型int，表示为长整型
    # 内置的type(）可以查看变量对应的对象类型
    # 内置的id()函数可以查看变量的内存空间地址
    # 数值的除法( /)总是返回一个浮点数，取整用 //，取余用 %
    # 在混合运算时，python会把整型转化为浮点数

# 非数字型：字符串、列表、元组、字典"""

"""
● list  列表
  ○ 用[]定义，可为空
  ○ 列表中可以存在不同类型的对象
  ○ 列表也支持切片，取一部分数据，也支持步长
  ○ 支持+和*，+将两个列表拼接一起，*重复输出N次
"""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list1 + list2)  # [1,2,3,'a','b','c']
print(list1 * 2)  # [1,2,3,1,2,3]

# 常用方法
list1.append(4)  # [1,2,3,4]  增加一个元素
list1.append('5')   # [1, 2, 3, 4, '5']
list1.pop(0)  # [2,3,4]    根据下标删除一个元素
list2.remove('a')  # ['b','c']  根据对象删除一个元素
list2.clear()  # []  清空列表
list3 = ['a', 'b', 'c', 'b']
result = list3.index('b')  # 结果为1，返回指定成员在list中第一次出现的位置下标
print(list3.count('b'))  # 结果为2，统计指定对象的个数
list3.sort()  # ['a','b','b','c'],升序
list3.sort(reverse=True)  # ['c','b','c','a'],降序
list3.reverse()  # ['b','c','b','a'],反序
