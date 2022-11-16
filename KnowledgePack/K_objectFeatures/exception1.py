# 捕获指定的单个异常
try:
    print('11111')
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)  # division by zero
print('22222222')

# 捕获指定的多个异常
try:
    print('11111')
    print(10 / 0)  # ZeroDivisionError
    print(1 +'a')   # TypeError
    # print(a)  	  # NameError
except (ZeroDivisionError, TypeError, NameError) as e:
    print(e)  # division by zero
print('22222222')

# 捕获已知和未知的所有的异常,也不推荐
import sys

try:
    print('11111')
    print(10 / 0)  # ZeroDivisionError
    print(1 +'a')   #TypeError
    # print(a)  	  #NameError
except:
    print(sys.exc_info())
print('22222222')

# 捕获所有已知异常，推荐
try:
    print('11111')
    print(10 / 0)
except Exception as e:
    print(e)
print('22222222')

