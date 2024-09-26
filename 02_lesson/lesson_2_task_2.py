def is_year_leap(y):
    return True if y % 4 == 0 else False


year = int(input('Введите год для проверки, является ли он високосный?: '))
examin = is_year_leap(year)
print(f'год {year}: {examin}')
