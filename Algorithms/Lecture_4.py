# coding: utf8

import random
# Функции

def hello():
    print('Hello!')

hello()

f = hello
f()

# Функция с обязательным параметром
def hello(name):
    print('Hello,', name)

hello('Alex')

f = hello
f('Al')

# Функция с не обязательным параметром
def hello(name='User'):
    print('Hello,', name)

hello()

# Возврат из функции
def max2(x, y):
    if x > y:
        return x
    return y

print(max2(3, 6))
print(max2(3, 3))

def max3(x, y, z):
    return max2(x, max2(y, z))

print(max3(5, 8, 5))
print(max3('ab', 'adc', 'abd'))

def hello_sep(name='World', sep='-'):
    print('Hello', name, sep=sep)

hello_sep()
hello_sep(sep='***')
hello_sep(sep='+', name='John')

# Стек вызовов
# A -> B -> C -> D
# |   |
# | D |
# | C |
# | B |
# | A |
# -----

# Структурное программирование
# Проектирование "сверху-вниз"
import graphics as gr
def build_house(window, upper_left_corner, width):
    '''
    Функция, которая рисует дом
    :return:
    '''
    height = calculate_sizes(width)

def calculate_sizes(width):
    pass

window = gr.GraphWin('Russian game', 300, 300)
build_house(window, gr.Point(100, 100), 100)
print('Yapi! The house is build!')

# Алгоритмы
# Метод грубой силы
def is_simple_number(x):
    ''' Определяет, является ли число простым.
    Если простое, то возвращает True, иначе -  False
    :param x: int>0
    :return: bool
    '''
    print(x, end=' - ')
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
        return True

print(is_simple_number(random.randint(1, 100)))

# Факторизация
def factorize_number(x):
    '''
    Раскладывает число на множители.
    Печатает их на экран
    :param x: int>0
    :return: x
    '''
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

factorize_number(random.randint(1, 100))