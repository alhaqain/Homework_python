lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

lst_filter = [a for a in lst if a < 30 and a % 3 == 0]

print(lst_filter)
