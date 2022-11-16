class Test1:
    def __init__(self):
        print('this is __init__')
        self.name = 'Tom'   # init初始化变量后，以这里为准，类内的变量将会被覆盖
        self.__age = 18
        self.age = 20

    sex = 'man'
    name = 'Mary'

    def __del__(self):
        print('this is __def__')

    def sleep(self):
        self.__study()
        print(self.age)
        print(self.__age)
    
    def __study(self):
        print('this is study()')


if __name__ == '__main__':
    test1 = Test1()
    test1.sleep()
    print(test1.age)  # age可在类外使用
    print(test1.sex)    # man
    print(test1.name)   # Tom,而不是Mary
    # print(test1.__age)  # 该输出是错误的，__age是私有变量，只能在类内部调用


