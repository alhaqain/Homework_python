def month_to_season(m):
    if 3 <= m <= 5:
        return 'Весна'
    elif 6 <= m <= 8:
        return 'Лето'
    elif 9 <= m <= 11:
        return 'Осень'
    else:
        return 'Зима'


m = int(input('Введите номер месяца от 1 до 12: '))
if 1 <= m <= 12:
    print(month_to_season(m))
else:
    print('Неверный номер месяца. Введите целое число от 1 до 12.')
