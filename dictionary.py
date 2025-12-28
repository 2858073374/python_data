""" 
日期：2025年 12月 28日  下午3:17  
"""
"""
创建和使用字典：字典的{}中的元素是以键值对的形式存在的，每个元素由:分隔的两个值构成，:前面是键，:后面是值
键是不可变类型（列表，集合），值可以是可变类型
"""
# person = {
#     'name': '王大锤',
#     'age': 55,
#     'height': 168,
#     'weight': 60,
#     'addr': '成都市武侯区科华北路62号1栋101',
#     'tel': '13122334455',
#     'emergence contact': '13800998877'
# }
# print(person)
#
# # dict函数(构造器)中的每一组参数就是字典中的一组键值对
# person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
# print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
#
# # 可以通过Python内置函数zip压缩两个序列并创建字典
# items1 = dict(zip('ABCDE', '12345'))
# print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
# items2 = dict(zip('ABCDE', range(1, 10)))
# print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
# for _ in items2:
#     print(_)#只对键进行循环
# # 用字典生成式语法创建字典
# items3 = {x: x ** 3 for x in range(1, 6)}
# print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""
字典的运算，字典里的值可以是列表也可以是字典，通过索引得到值
# """
# person = {
#     'name': '王大锤',
#     'age': 55,
#     'height': 168,
#     'weight': 60,
#     'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
#     'car': {
#         'brand': 'BMW X7',
#         'maxSpeed': '250',
#         'length': 5170,
#         'width': 2000,
#         'height': 1835,
#         'displacement': 3.0
#     }
# }
# print(person)
#print('~~~~~~~~~~~~~')
# person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
# # 成员运算
# print('name' in person)  # True
# print('tel' in person)   # False
# # 索引运算
# print(person['name'])
# print(person['addr'])
# person['age'] = 25
# person['height'] = 178
# person['tel'] = '13122334455'
# person['signature'] = '你的男朋友是一个盖世英雄，他会踏着五彩祥云去迎娶你的闺蜜'
# print(person)
# # 循环遍历，直接对person循环只能得到key键，用列表的方式来输出值****
# for _ in person:
#     print(f'{_}:\t{person[_]}')
"""
字典的方法
"""
# person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
# print(person.get('name'))       # 王大锤
# print(person.get('sex'))        # None
# print(person.get('sex', True))  # True
# print('~~~~~~~~~~~~~~~~~')
#利用关键字key,values,items***
# person = {'name': '王大锤', 'age': 25, 'height': 178}
# print(person.keys())    # dict_keys(['name', 'age', 'height'])
# print(person.values())  # dict_values(['王大锤', 25, 178])
# print(person.items())   # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
# for key, value in person.items():
#     print(f'{key}:\t{value}')
# print('~~~~~~~~~~~~~~~~~')
#以下操作跟集合相同*******
#执行x.update(y)操作时，x跟y相同的键对应的值会被y中的值更新，而y中有但x中没有的键值对会直接添加到x中
# person1 = {'name': '王大锤', 'age': 55, 'height': 178}
# person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# person1.update(person2)
# print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
# print('~~~~~~~~~~~~~~~~~')
# person1 = {'name': '王大锤', 'age': 55, 'height': 178}
# person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# person1 |= person2
# print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
"""
删除与清空,与列表，字典用法相同，由于字符串是不可变量故不可用该方法
"""
# person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
# print(person.pop('age'))  # 25
# print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
# print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
# print(person)             # {'name': '王大锤', 'height': 178}
# person.clear()
# print(person)             # {}
"""
字典的应用
"""
sentence = input('请输入一段话: ')
counter = {}
for _ in sentence:
    if 'A' <= _ <= 'Z' or 'a' <= _ <= 'z':
        counter[_] = counter.get(_, 0) + 1
sorted_keys = sorted(counter, key=counter.get, reverse=True)
for key in sorted_keys:
    print(f'{key} 出现了 {counter[key]} 次.')
# print('~~~~~~~~~~~')
# stocks = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# stocks2 = {key: value for key, value in stocks.items() if value > 100}
# print(stocks2)