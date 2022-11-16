"""
#有异常，异常之后的代码不执行（print('33333')）
#有异常，else不执行
#无异常，else执行
#finally，无论是否有异常，都执行
"""

try:
    print('11111')
    # print(10/0)
    print('33333')
except Exception as e:  # 有异常才会执行
    print(e)
    # raise      # 捕获到异常，可以使用raise关键字继续抛出异常，后续代码就不会执行
else:  # 无异常才执行
    print('this is else')
finally:  # 是否有异常都执行
    print('this is finally')
print('22222222')

"""
#自定义异常
#循环打印1-10，等于5时，直接退出
"""

for i in range(1, 11):
    if i == 5:
        try:
            raise TypeError('自定义异常！')
        except Exception as e:
            break
    else:
        print(i)
