# Ввод чисел
d_1 = int(input('1-е число             | '))
d_2 = int(input('2-е число             | '))
d_3 = int(input('3-е число             | '))
d_4 = int(input('4-е число             | '))
d_5 = int(input('5-е число             | '))
d_6 = int(input('6-е число             | '))
d_7 = int(input('7-е число             | '))
d_8 = int(input('8-е число             | '))
d_9 = int(input('9-е число             | '))
d_10 = int(input('10-е число            | '))

# Нахождение максимальных и минимальных значений
maximum = max(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)
minimum = min(d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9, d_10)

# Ввод отступов
print('————————————————————————————————')

# Вывод результата
print('Максимальное значение |', maximum)
print('Минимальное значение  |', minimum)
