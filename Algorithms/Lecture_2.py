# Дизъюктивная нормальная форма
x = [0, 0, 0, 0, 1, 1, 1, 1]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 1, 0, 1, 0, 1, 0, 1]
f = [1, 0, 0, 1, 0, 0, 1, 0]

def f_1(x, y, z):
    return (not x and not y and not z)

def f_2(x, y, z):
    return (not x and y and z)

def f_3(x, y, z):
    return (x and y and not z)

print('f1')
for i in range(len(x)):
    print(f_1(x[i], y[i], z[i]))
print('\n')

print('f2')
for i in range(len(x)):
    print(f_2(x[i], y[i], z[i]))
print('\n')

print('f3')
for i in range(len(x)):
    print(f_3(x[i], y[i], z[i]))
print('\n')

print('f = f1 + f2 + f3')
for i in range(len(x)):
    print(f_1(x[i], y[i], z[i]) or f_2(x[i], y[i], z[i]) or f_3(x[i], y[i], z[i]))
print('\n')

# Законы алгебры логики
print('\nВзаимодействие с константами')
print(0 or object) # Лож или объект равно объект
print(1 or object) # Истина или объект равно Истина (истеннее чем Истина быть не может)
print(0 and object) # Лож и объект равно Лож
print(1 and object) # Истина и объект равно объект

# Простые
print('\nЗакон повторения')
print(object or object) # Объект плюс Объект равно Объект
print(object and object) # Объект умножить Объект равно Объект
print(object or not object) # Объект плюс не Объект равно Объект
print(object and not object) # Объект умножить не Объект равно Лож

print('\nЗакон поглощения')
print(object and (object or True)) # Объект умножить Объект плюс Истина равно Объект
print(object or object and True) # Объект плюс Объект умножить Истина равно Объект

print('\nСвойства "и" и "или"')
print(True and object == object and True)
print(True or object == object or True)

print('\nЗакон Де Моргана')
print(True and object == object and True)
print(True or object == object or True)