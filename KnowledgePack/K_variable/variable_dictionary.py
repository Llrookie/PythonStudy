"""
● dictionary  字典
  ○ dict1 = {}，可定义一个空字典
"""

dict1 = {'name': '张三', 'age': 18}
print(dict1)  # {'name': '张三', 'age': 18}
dict1['age'] = 28  # 修改键值为age的值
print(dict1)  # {'name': '张三', 'age': 28}
print(dict1['name'])  # 无序，不支持下标  --张三
print(dict1.keys())  # 获取所有的key值  dict_keys(['name', 'age'])
print(dict1.values())  # 获取所有的value值  dict_values(['张三', 28])
print(dict1.get('name'))  # 根据key值获取value值   张三
dict1.pop('name')  # 删除指定的键值对
print(dict1)  # {'age': 28}
dict1.clear()  # 清空字典

# fromkeys()方法
# 用于创建一个新的字典
# fromkeys 方法只用来创建新字典，不负责保存。当通过一个字典来调用 fromkeys 方法时，如果需要后续使用一定记得给他复制给其他的变量。
dict = {}
seq = ('Google', 'Runoob', 'Taobao')
dict1 = dict.fromkeys(seq)
print(dict1)    # {'Google': None, 'Taobao': None, 'Runoob': None}
dict2 = dict.fromkeys(seq, 10)
print(dict2)    # {'Google': 10, 'Taobao': 10, 'Runoob': 10}

# key有重复时，以最后的为准
dict1 = {'name': '张三', 'age': 18, 'name': '李四'}
print(dict1)  # {'name': '李四', 'age': 18}
