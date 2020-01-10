# coding: utf8

import random

# Системы счисления
base = 7
x = random.randint(0, 1000)
print('x is ', x)
while x > 0:
    digit = x % base
    print(digit, end='')
    x //= base

