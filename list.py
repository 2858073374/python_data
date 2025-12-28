""" 
日期：2025年 12月 27日  上午11:12  
"""
"""
将一颗色子掷6000次，统计每种点数出现的次数
"""
# import random
# #counters=[0,0,0,0,0,0]
# counters = [0] * 6
# # 模拟掷色子记录每种点数出现的次数
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     counters[face - 1] += 1
# # 输出每种点数出现的次数
# for face in range(1, 7):
#     print(f'{face}点出现了{counters[face - 1]}次')
"""
列表的添加与插入
"""
# languages = ['Python', 'Java', 'C++']
# languages.append('JavaScript')
# print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
# languages.insert(1, 'SQL')
# print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
"""
列表内容的删除与清空
"""
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
# if 'Java' in languages:
#     languages.remove('Java')
# if 'Swift' in languages:
#     languages.remove('Swift')
# print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
# languages.pop()
# temp = languages.pop(1)
# print(temp)       # SQL
# languages.append(temp)
# print(languages)  # ['Python', C++', 'SQL']
# languages.clear()
# print(languages)  # []
# items = ['Python', 'Java', 'C++']
# del items[1]
# print(items)  # ['Python', 'C++']
"""
列表中的查找与计数
"""
# items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
# print(items.index('Python'))     # 0
# # 从索引位置1开始查找'Python'
# print(items.index('Python', 1))  # 5
# print(items.count('Python'))     # 2
# print(items.count('Kotlin'))     # 1
# print(items.count('Swfit'))      # 0
# # 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list
"""
排序与反转
"""
# items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
# items.sort()
# print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
# items.reverse()
# print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']
"""
两种列表的生成方法
"""
# nums1 = []
# for i in range(5):
#     nums1.append(i)
# nums2 = []
# for num in nums1:
#     nums2.append(num ** 2)#num的平方
# nums3 = [num ** 2 for num in nums1]
# print(nums2)#[0, 1, 4, 9, 16]
# print(nums3)#[0, 1, 4, 9, 16]
# print(nums1)
"""
列表的嵌套与嵌套的一般程序
"""
# scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
# print(scores[0])
# print(scores[0][1])
#
# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
#     scores.append(temp)
# print(f'scores={scores}')
"""
随机嵌套生成的标准式子
"""
# import random
# scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
# print(scores)
"""
双色球随机选号程序
"""
# import random
#
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# # 从红色球列表中随机抽出6个红色球（无放回抽样）
# selected_balls = random.sample(red_balls, 6)
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     #0>2d在数字不到两位时，在前面补上一个0
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 从蓝色球列表中随机抽出1个蓝色球
# blue_ball = random.choice(blue_balls)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

# import random
# red_ball=[i for i in range(1,33)]
# blue_ball=[i for i in range(1,11)]
# se_red_ball=random.sample(red_ball,6)
# se_red_ball.sort()
# for ball in se_red_ball:
#      #0>2d在数字不到两位时，在前面补上一个0
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# se_blue_ball=random.choice(blue_ball)
# print(f'\033[034m{se_blue_ball:0>2d}\033[0m')
"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)