"""
def 函数名(参数列表):
	函数体
"""


# 示例1  带有形参
def area(weight, heignt):
    return weight * heignt


# 没有return的时候，函数默认返回None

print(area(5, 4))   # 20


# 示例2  不带形参
def print_name():
    print("Python练习")


# 示例3  return多个结果
def method1(x, y):
    return x + y, x * y, x - y, x / y


result = method1(5, 2)  # (7, 10, 3, 2.5)，用一个对象来接受返回值，这个对象的类型为元组类型tuple
result0 = result[1]  # 10

result1, result2, result3, result4 = method1(5, 2)  # 也可用多个对象来接受返回值
