""" 
日期：2025年 12月 28日  下午12:10  
"""
"""
集合中的元素具有无序性，互异性，确定性的特点
"""
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
#
# set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
# print(set2)
#
# set3 = set('hello')
# print(set3)#{'l', 'h', 'e', 'o'}
#
# set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
# print(set4)#{1, 2, 3}
#
# set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
# print(set5)

"""
二元运算：主要指集合的交集、并集、差集、对称差等运算
"""
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {2, 4, 6, 8, 10}
# #交集
# print(set1 & set2)                      # {2, 4, 6}
# print(set1.intersection(set2))          # {2, 4, 6}
# 并集
# print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 差集
# print(set1 - set2)                      # {1, 3, 5, 7}
# print(set1.difference(set2))            # {1, 3, 5, 7}
# 对称差：返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
# print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
# print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

# set1 = {1, 3, 5, 7}
# set2 = {2, 4, 6}
# set1 |= set2
# # set1.update(set2)
# print(set1)  # {1, 2, 3, 4, 5, 6, 7}
# set3 = {3, 6, 9}
# set1 &= set3
# # set1.intersection_update(set3)
# print(set1)  # {3, 6}
# set2 -= set1
# # set2.difference_update(set1)
# print(set2)  # {2, 4}

"""
set1 < set2判断set1是不是set2的真子集，
set1 <= set2判断set1是不是set2的子集
set2 > set1判断set2是不是set1的超集。
通过set1.issubset(set2)判断set1是不是set2的子集
通过set2.issuperset(set1)判断set2是不是set1的超集
"""
# set1 = {1, 3, 5}
# set2 = {1, 2, 3, 4, 5}
# set3 = {5, 4, 3, 2, 1}
#
# print(set1 < set2)   # True
# print(set1 <= set2)  # True
# print(set2 < set3)   # False
# print(set2 <= set3)  # True
# print(set2 > set1)   # True
# print(set2 == set3)  # True
#
# print(set1.issubset(set2))    # True
# print(set2.issuperset(set1))  # True

"""
集合元素的增加与删除，清空
"""
# set1 = {1, 10, 100}

# 添加元素,list列表使用.append来进行添加
# set1.add(1000)
# set1.add(10000)
# print(set1)  # {1, 100, 1000, 10, 10000}
#
# 删除元素，关键字与list相同
# set1.discard(10)
# if 100 in set1:
#     set1.remove(100)
# print(set1)  # {1, 1000, 10000}
#
# 清空元素
# set1.clear()
# print(set1)  # set()

#isdisjoint判断两个集合有没有相同的元素，没有相同元素，该方法返回True，否则该方法返回False
# set1 = {'Java', 'Python', 'C++', 'Kotlin'}
# set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
# set3 = {'HTML', 'CSS', 'JavaScript'}
# print(set1.isdisjoint(set2))  # False
# print(set1.isdisjoint(set3))  # True

"""
不可变集合，set跟frozenset的区别就如同list跟tuple的区别
"""
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False