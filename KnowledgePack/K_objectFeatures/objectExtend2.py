"""
super().函数名     #可以在子类中调用父类的方法
super().变量名     # 可以在子类中调用父类的变量
"""


class Father:
    def eat(self):
        print('this is Father eat()')

    def sleep(self):
        print('this is Father sleep()')

    name = 'Tom'
    age = 18


class Son(Father):
    def eat(self):
        print('this is Son eat()')

    def sleep(self):
        print('this is Son sleep()')
        super().sleep()
        print(super().name, super().age)

    name = 'Mary'
    age = 20


if __name__ == '__main__':
    son = Son()
    son.sleep()
    print(son.name, son.age)

"""
this is Son sleep()
this is Father sleep()
Tom 18
Mary 20
"""