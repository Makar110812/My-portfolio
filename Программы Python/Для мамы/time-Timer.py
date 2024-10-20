# Импорт времени
import time

# Ввод времени таймера
i = int(input('Введите время таймера в секундах: '))

# Таймер
for n in range(i + 1):
    print(i - n)
    time.sleep(1)
    if i - n == 0:
        print('FINISH')
        exit(i)
