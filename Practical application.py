""" 
日期：2025年 12月 29日  下午2:06  
"""
"""
生成随机验证码的函数
"""
import random
import string

# ALL_CHARS = string.digits + string.ascii_letters
#
# #generate_code(*, code_len=4)，‘*’表示code_len这个参数只能以关键字参数提供
# def generate_code(*, code_len=4):
"""
生成指定长度的验证码
:param code_len: 验证码的长度(默认4个字符)
:return: 由大小写英文字母和数字构成的随机验证码字符串
"""
#     return ''.join(random.choices(ALL_CHARS, k=code_len))
#
# for _ in range(5):
#     print(generate_code(code_len=6))

"""
判断素数
num后面的: int用来标注参数的类型，虽然它对代码的执行结果不产生任何影响，
但是很好的增强了代码的可读性。
同理，参数列表后面的-> bool用来标注函数返回值的类型，
它也不会对代码的执行结果产生影响，但是却让我们清楚的知道，调用函数会得到一个布尔值
"""
def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def lcm(x: int, y: int) -> int:
    """求最小公倍数"""
    return x * y // gcd(x, y)

def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x

"""
双色球选号
"""
"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]


def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls
"""
random模块的sample和choices函数都可以实现随机抽样，
sample实现无放回抽样，这意味着抽样取出的元素是不重复的，必须指定个数。
choices实现有放回抽样，这意味着可能会重复选中某些元素
"""

def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())