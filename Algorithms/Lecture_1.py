# coding: utf8
x = 3
while x > 0:
    y = x
    while y > 0:
        y -= 1
        print(y)
    x -= 1
print('stop')

x = 'reversed'
x_reversed = ''.join([x[i] for i in range(len(x) - 1, -1, -1)])
print(x_reversed)
