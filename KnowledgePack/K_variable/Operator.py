"""
● 算数运算符
  ○ 加 + 减 - 乘 * 除 / 取整 // 取余 % 次方 **
● 比较运算符
  ○ >,<,>=,<=,!=,==
● 赋值运算符
  ○ =,+=,-=,*=,/=,**=,//=,%=
● 位运算符
  ○ 按位与&，按位或|，按位异或^（不同为真）,按位取反~,左移<<，右移>>
● 逻辑运算符
  ○ and  or   not
● 成员运算符
  ○ in,not in
● 身份运算符
  ○ is,is not
  """

print(5 / 2)  # 2.5
print(5 // 2)  # 2
print(5 % 2)  # 1
print(5 ** 2)  # 25
print(pow(5, 2))  # 25

# 判断某一成员是否在某一集合中
list1 = ['a', 'b', 'c']
if 'b' in list1:
    print("yes")
else:
    print('no')
if 'd' not in list1:
    print('yes')
else:
    print('no')

# 身份运算符
a = 1
b = 2
print(id(a), id(b))  # 2328821459248 2328821459280
print(a is not b)  # True

# umber、tuple、string类型，值相同，内存地址就相同
a = 1
b = 1
print(id(a), id(b))  # 2033035667760 2033035667760
print(a is b)  # True
print(a is not b)  # False

# list、set、dict类型，值相同，内存地址不相同
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
print(id(a), id(b))  # 2828877181120 2828877181824
print(a is b)  # False
print(a == b)  # True
