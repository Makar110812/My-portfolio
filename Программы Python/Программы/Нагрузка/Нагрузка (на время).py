input('Для запуска нажмите ENTER. ')      # Подтверждение запуска программы
from math import factorial                # Импорт факториала из библиотеки "math"
from sys import set_int_max_str_digits    # Импорт лимита из библиотеки "sys"
from time import time                     # Импорт секундомера из библиотеки "time"
set_int_max_str_digits(2147483647)        # Изменение лимита до максимально возможного значения
n = 0                                     # Установка начального значения переменной "n" (0)
while True:                               # Создание замкнутого цикла
    n = n + 1                             # Прибавление к переменной "n" 1
    print(factorial(n))                   # Нахождение факториала от переменной "n"
    if (len(str(n))) == 2000000000:       # Если значение символов переменной "n" превысит лимит, то
        break                             # Выйти из цикла
print('Производительность компьютера оценена в', time, 'баллов. (Чем меньше, тем лучше.)')
