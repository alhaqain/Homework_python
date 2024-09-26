import math
x = float(input('Введите значение стороны квадрата: '))

a = math.ceil(x)


def square(a):
    return a * a


print(f'Площадь квадрата: {square(a)}')
