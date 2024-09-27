import math


def square(a):
    return math.ceil(a * a)


x = float(input('Введите значение стороны квадрата: '))
print(f'Площадь квадрата: {square(x)}')
