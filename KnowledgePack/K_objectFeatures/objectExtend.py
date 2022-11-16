"""
# python可以多继承
# 继承调用顺序：从左到右，从深度(纵向)到广度(横向)
# 继承父类时，在子类后括号加上父类就行  eg：class Son(Father1,Father2)
# 父类需写在子类前面
"""


class grandFather:
    name = '老张'

    def eat(self):
        print('grandFather : eat')


class Father1(grandFather):
    name = '张1'

    def eat(self):
        print('Father1 : eat')


class Father2:
    name = '张2'

    def eat(self):
        print('Father2 : eat')

    def paly(self):
        print('Father2 : play')


class Son(Father1, Father2):    # 继承多个父类，找方法找第一个父类的
    name = '小张'

    def eat(self):
        print('son : eat')


if __name__ == '__main__':
    son = Son()
    son.eat()  # 先找子类自己的方法，没有再找父类，父类没有再找父类的父类，有多个父类按顺序找
    son.paly()  # Father2 : play
