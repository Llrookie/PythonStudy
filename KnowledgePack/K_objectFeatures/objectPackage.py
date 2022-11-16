# 构造方法和析构方法在对象实例化是就会调用，先执行init，最后执行del
# 命名规则：包名、模块名一般小写；类名每个单词首字母大写；方法名除首个单词小写外，其他单词首字母大写

class Person:
    def __init__(self):  # 构造方法，最先执行，通常用来初始化一些对象
        # self.name = 'zhangsan'  # 属性定义在构造方法中，要加self
        # self.__age = 20  		 # 构造方法中，也可以定义为私有属性
        print('this is init()')

    name = 'zhangsan'
    __age = 18  # 私有属性，只能在类的内部调用
    age = 20

    def __study(self):  # 私有方法，只能在类的内部调用
        print('this is study()')

    def sleep(self):
        print('this is sleep()')
        print(self.__age)
        self.__study()

    def __del__(self):  # 析构方法，通常最后执行
        print('this is del()')


if __name__ == '__main__':
    p = Person()  # 对象实例化时，会执行init方法和del方法
    p.sleep()
    print(p.age)
    print(p.name)

"""
输出结果：
    this is init()
    this is sleep()
    18
    this is study()
    20
    zhangsan
    this is del()
"""
