""" 
日期：2025年 12月 29日  上午10:35  
"""
"""
输入m和n，计算组合数C(m,n)的值
"""
"""不使用函数"""
# m = int(input('m = '))
# n = int(input('n = '))
# 计算m的阶乘
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# 计算n的阶乘
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# 计算m-n的阶乘
# fk = 1
# for num in range(1, m - n + 1):
#     fk *= num
# 计算C(M,N)的值
# print(fm // fn // fk)
"""使用函数"""
# 通过关键字def定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
# def fac(num):
#     result = 1
#     for n in range(2, num + 1):
#         result *= n
#     return result
#
# m = int(input('m = '))
# n = int(input('n = '))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
# print(fac(m) // fac(n) // fac(m - n))
"""
使用库中的函数
"""
#利用‘as’简化函数名
# from math import factorial as f
#
# m = int(input('m = '))
# n = int(input('n = '))
# print(f(m) // f(n) // f(m - n))

"""
函数的参数:位置参数和关键字参数：两种传参方法,参数的默认值
"""

# def make_judgement(a, b, c):
#     """判断三条边的长度能否构成三角形"""
#     return a + b > c and b + c > a and a + c > b
#按照从左到右的顺序依次传入，而且传入参数的数量必须和定义函数时参数的数量相同
# print(make_judgement(1, 2, 3))  # False
# print(make_judgement(4, 5, 6))  # True
# print('~~~~~~~~~~')
#使用关键字参数，通过“参数名=参数值”的形式为函数传入参数
# print(make_judgement(b=2, c=3, a=1))  # False
# print(make_judgement(c=6, b=4, a=5))  # True

#在参数列表中用'/'设置强制位置参数,用'*'设置命名关键字参数
#'/'只能按照参数位置来接收参数值的参数,'*'只能通过“参数名=参数值”的方式来传递和接收参数
# def make_judgement(a, b, c, /):   def make_judgement(*,a, b, c):
#     """判断三条边的长度能否构成三角形"""
#     return a + b > c and b + c > a and a + c > b

"""
参数的默认值,直接对形参进行赋值
"""
# from random import randrange
# # 定义摇色子的函数
# # 函数的自变量（参数）n表示色子的个数，默认值为2
# # 函数的因变量（返回值）表示摇n颗色子得到的点数
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randrange(1, 7)
#     return total
# # 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
# print(roll_dice())
# # 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
# print(roll_dice(3))
# print('~~~~~~~~~~')
# 带默认值的参数必须放在不带默认值的参数之后*****
# def add(a=0, b=0, c=0):
#     """三个数相加求和"""
#     return a + b + c
# # 调用add函数，没有传入参数，那么a、b、c都使用默认值0
# print(add())         # 0
# # 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
# print(add(1))        # 1
# # 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
# print(add(1, 2))     # 3
# # 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
# print(add(1, 2, 3))  # 6
"""
可变参数，可以向函数传入0个或任意多个参数，不受数据类型限制，通过星号表达式语法让函数支持可变参数*****
"""
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
# def add(*args):
#     total = 0
#     # 对保存可变参数的元组进行循环遍历
#     for val in args:
#         # 对参数进行了类型检查（数值型的才能求和）
#         if type(val) in (int, float):
#             total += val
#     return total
#
#
# # 在调用add函数时可以传入0个或任意多个参数
# print(add())         # 0
# print(add(1))        # 1
# print(add(1, 2, 3))  # 6
# print(add(1, 2, 'hello', 3.45, 6))  # 12.45
#print('~'*10)
"""
通过“参数名=参数值”的形式传入若干个参数
"""
# 参数列表中的**变量可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
# def foo(*args, **k):
#     print(args)#(3, 2.1, True)
#     print(k)#{'name': '骆昊', 'age': 43, 'gpa': 4.95}
#     print(args,k)#(3, 2.1, True) {'name': '骆昊', 'age': 43, 'gpa': 4.95}
# foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)
"""
用模块管理函数
"""
#多个文件时
def foo():
    print('hello, world!')

def foo():
    print('goodbye, world!')

import module1 as m1
import module2 as m2

m1.foo()  # hello, world!
m2.foo()  # goodbye, world!
print('~'*10)
from module1 import foo as f1
from module2 import foo as f2
f1()
f2()


