""" 
日期：2025年 12月 27日  下午5:53  
"""
"""
元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销。
通常不可变类型在创建时间上优于对应的可变类型,在运算上更快。
"""
# # 定义一个三元组
# t1 = (35, 12, 98)
# 定义一个四元组
# t2 = ('骆昊', 45, True, '四川成都')
#
# # 查看变量的类型
# print(type(t1))  # <class 'tuple'>
# print(type(t2))  # <class 'tuple'>
#
# # 查看元组中元素的数量
# print(len(t1))  # 3
# print(len(t2))  # 4
#
# # 索引运算
# print(t1[0])    # 35
# print(t1[2])    # 98
# print(t2[-1])   # 四川成都
#
# # 切片运算,‘:’前默认有0
# #0 to 1
# print(t2[:2])   # ('骆昊', 45)
#::n代表取值间隔为3，每隔两个取一个，即第三个
# print(t2[::3])  # ('骆昊', '四川成都')
#
# # 循环遍历元组中的元素
# for elem in t1:
#     print(elem)
#
# # 成员运算
# print(12 in t1)         # True
# print(99 in t1)         # False
# print('Hao' not in t2)  # True
#
# # 拼接运算
# t3 = t1 + t2
# print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')
#
# # 比较运算
# print(t1 == t3)            # False
# print(t1 >= t3)            # False
# print(t1 <= (35, 11, 99))  # False
"""
()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，
否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数
"""
# a = ()
# print(type(a))  # <class 'tuple'>
# b = ('hello')
# print(type(b))  # <class 'str'>
# c = (100)
# print(type(c))  # <class 'int'>
# d = ('hello', )
# print(type(d))  # <class 'tuple'>
# e = (100, )
# print(type(e))  # <class 'tuple'>
"""
打包和解包
"""
# 打包操作
# a = 1, 10, 100
# print(type(a))  # <class 'tuple'>
# print(a)        # (1, 10, 100)
# # 解包操作
# i, j, k = a
# print(i, j, k)  # 1 10 100
"""
利用列表来解包‘*变量’解包变量数量<=元组元数
"""
# a = 1, 10, 100, 1000
# i, j, *k = a
# print(i, j, k)        # 1 10 [100, 1000]
# i, *j, k = a
# print(i, j, k)        # 1 [10, 100] 1000
# *i, j, k = a
# print(i, j, k)        # [1, 10] 100 1000
# *i, j = a
# print(i, j)           # [1, 10, 100] 1000
# i, *j = a
# print(i, j)           # 1 [10, 100, 1000]
# i, j, k, *l = a
# print(i, j, k, l)     # 1 10 100 [1000]
# i, j, k, l, *m = a
# print(i, j, k, l, m)  # 1 10 100 1000 []

# a, b, *c = range(1, 10)
# print(a, b, c)  #1 2 [3, 4, 5, 6, 7, 8, 9]
# a, b, c = [1, 10, 100]
# print(a, b, c)
# a, *b, c = 'hello'
# print(a, b, c) #h ['e', 'l', 'l'] o
"""
元组与列表的互换
"""
# infos = ('骆昊', 43, True, '四川成都')
# # 将元组转换成列表
# print(list(infos))  # ['骆昊', 43, True, '四川成都']
#
# frts = ['apple', 'banana', 'orange']
# # 将列表转换成元组
# print(tuple(frts))  # ('apple', 'banana', 'orange')
