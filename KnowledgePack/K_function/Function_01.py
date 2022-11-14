# 全局变量和局部变量
a = 1


def method():
    global a  # 在函数体中声明，这是一个全局变量
    a = 2
    print(a)


method()  # 输出为2
print(a)  # 输出为2
#####################################
a = 1


def method():
    a = 2
    print(a)


method()  # 输出为2
print(a)  # 输出为1

# 可变对象和不可变对象充当形参
# 不可变对象：数值型、字符串、元组
# 可变对象：集合、列表、字典

a = [1]


def method(a):
    a.append(2)
    print(a)


method(a)  # [1, 2]
print(a)  # [1, 2]
#####################################
a = 1


def method(a):
    a = 2
    print(a)


method(a)  # 2
print(a)  # 1


# 不定长参数，可以接收0~多个参数
def add(*number):
    total = 0
    for i in number:
        total += i
    return total


if __name__ == "__main__":
    print(add(1, 2, 3))  # 6

"""
匿名函数 使用场景，单行语句，懒得起名，一次性使用
格式：lambda 形参：表达式
#匿名函数的形参为0~多个
"""
sum = lambda x, y: x + y
if __name__ == "__main__":
    print(sum(2, 3))  # 结果为5
