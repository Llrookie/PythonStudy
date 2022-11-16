"""
#对象不同，调用同一方法会有不同结果
#先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止
"""


class Father:
    def study(self):
        print('father study()')


class Son(Father):
    def study(self):
        print('son study()')


if __name__ == '__main__':
    def method(obj):
        obj.study()

    fa = Father()
    son = Son()
    method(fa)  # father study()
    # 如果Son类中没有study()方法，则会调用父类的study()
    method(son)  # son study()
