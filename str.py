""" 
日期：2025年 12月 28日  上午9:57  
"""
"""
字符串的输出以及转义字符‘\’的使用（其使后面的字符不再是它原来的意义）
"""
# s1 = 'hello, world!'
# s2 = "你好，世界！❤️"
# s3 = '''hello,
# wonderful
# world!'''
# print(s1)
# print(s2)
# print(s3)
# s1 = '\'hello, world!\''
# s2 = '\\hello, world!\\'
# print(s1)
# print(s2)
"""
 以r或R开头的字符串，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义
"""
# s1 = '\it \is \time \to \read \now'
# s2 = r'\it \is \time \to \read \now'
# print(s1)
# print(s2)
#在\后面还可以跟一个八进制或者十六进制数来表示字符，\u后面跟 Unicode 字符编码表示字
# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1)
# print(s2)
"""
字符串的运算
"""
#拼接+，乘*
# s1 = 'hello' + ', ' + 'world'
# print(s1)    # hello, world
# s2 = '!' * 3
# print(s2)    # !!!
# s1 += s2
# print(s1)    # hello, world!!!
# s1 *= 2
# print(s1)    # hello, world!!!hello, world!!!
#比较运算。使用ord函数来获得字符对应的编码，字符串的大小比较比的是每个字符对应的编码的大小，第一个相同则进行顺位比较
# s1 = 'a whole new world'
# s2 = 'hello world'
# print(s1 == s2)             # False
# print(s1 < s2)              # True
# print(s1 == 'hello world')  # False
# print(s2 == 'hello world')  # True
# print(s2 != 'Hello world')  # True
# s3 = '骆昊'
# print(ord('骆'))            # 39558
# print(ord('昊'))            # 26122
# s4 = '王大锤'
# print(ord('骆'))            # 29579
# print(ord('大'))            # 22823
# print(ord('锤'))            # 38180
# print(s3 >= s4)             # True
# print(s3 != s4)             # True
#跟列表类型一样，in和not in称为成员运算符，会产生布尔值True或False
# s1 = 'hello, world'
# s2 = 'goodbye, world'
# print('wo' in s1)      # True
# print('wo' not in s2)  # False
# print(s2 in s1)        # False
# #获取字符长度
# s = 'hello, world'
# print(len(s))                 # 12
# print(len('goodbye, world'))  # 14

#索引和切片
# s = 'abc123456'
# n = len(s)
# print(s[0], s[-n])    # a a
# print(s[n-1], s[-1])  # 6 6
# print(s[2], s[-7])    # c c
# print(s[5], s[-4])    # 3 3
# print(s[2:5])         # c12
# print(s[-7:-4])       # c12
# print(s[2:])          # c123456
# print(s[:2])          # ab
# print(s[::2])         # ac246
#字符串的反向输出
# print(s[::-1])        # 654321cba
"""
字符串的方法
"""
#大小写变换
# s1 = 'hello, world!'
# # 字符串首字母大写
# print(s1.capitalize())  # Hello, world!
# # 字符串每个单词首字母大写
# print(s1.title())       # Hello, World!
# # 字符串变大写
# print(s1.upper())       # HELLO, WORLD!
# s2 = 'GOODBYE'
# # 字符串变小写
# print(s2.lower())       # goodbye
# # 检查s1和s2的值
# print(s1)               # hello, world
# print(s2)               # GOODBYE

#字符串中的空格也占一个位置。使用字符串的find或index方法均可以进行查找操作
# 还有逆向查找（从后向前查找）的版本，分别是rfind和rindex，用法不变
# s = 'hello, world!'
# print(s.find('or'))      # 8
# print(s.find('or', 9))   # -1
# print(s.find('of'))      # -1
# print(s.index('or'))     # 8
# print(s.index('or', 9))  # ValueError: substring not found

#isdigit用来判断字符串是不是完全由数字构成的，isalpha用来判断字符串是不是完全由字母构成的，isalnum用来判断字符串是不是由字母和数字构成的
# s1 = 'hello, world!'
# print(s1.startswith('He'))   # False
# print(s1.startswith('hel'))  # True
# print(s1.endswith('!'))      # True
# s2 = 'abc123456'
# print(s2.isdigit())  # False
# print(s2.isalpha())  # False
# print(s2.isalnum())  # True

#格式化
# s = 'hello, world'
# print(s.center(20, '*'))  # ****hello, world****
# print(s.rjust(20))        #         hello, world
# print(s.ljust(20, '~'))   # hello, world~~~~~~~~
# print('33'.zfill(5))      # 00033
# print('-33'.zfill(5))     # -0033
#
# a = 321
# b = 123
# print('{0} * {1} = {2}'.format(a, b, a * b))
# c = 321
# d = 123
# print(f'{c} * {d} = {c * d}')

#修剪
# s1 = '   jackfrued@126.com  '
# print(s1.strip())      # jackfrued@126.com
# s2 = '~你好，世界~'
# print(s2.lstrip('~'))  # 你好，世界~
# print(s2.rstrip('~'))  # ~你好，世界

#替换replace
# s = 'hello, good world'
# print(s.replace('o', '@'))     # hell@, g@@d w@rld
# print(s.replace('o', '@', 1))  # hell@, good world
# a='我住在河南zhengzhou'
# print(a.replace('z','h',2))#我住在河南hhenghhou

#split方法将一个字符串拆分为多个字符串（放在一个列表中）
#也可以使用字符串的join方法将列表中的多个字符串连接成一个字符串
# s = 'I love you'
# words = s.split()
# #words为一个三元数组
# for _ in range(len(words)):
#     print(words)     # ['I', 'love', 'you']
# for _ in range(len(words)):
#     print(words[_],end=' ')#I love you
# print('~'.join(words))  # I~love~you
# print('~~~~~~~~~~~~~')
# s = 'I#love#you#so#much'
# words = s.split('#')
# print(words)  # ['I', 'love', 'you', 'so', 'much']
# words = s.split('#', 2)
# print(words)  # ['I', 'love', 'you#so#much']

#编码encode和解码decode
a = '骆昊'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe9\xaa\x86\xe6\x98\x8a'
print(c)                  # b'\xc2\xe6\xea\xbb'
print(b.decode('utf-8'))  # 骆昊
print(c.decode('gbk'))    # 骆昊