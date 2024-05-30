import time
def indent(n):
    for _ in range(n):
        print()
print('1   | 1 секунда')
print('60  | 1 минута')
print('3600| 1 час')
indent(1)
period = int(input('На какое время (в секундах) поставить таймер? (введите 0 для секундомера) '))
if period == 0:
    n = 0
    while True:
        indent(50)
        print(n)
        n = n + 1
        time.sleep(1)
if period > 0:
    while True:
        indent(50)
        print(period)
        period = period - 1
        if period == 0:
            print('Время вышло!')
            break
        time.sleep(1)
