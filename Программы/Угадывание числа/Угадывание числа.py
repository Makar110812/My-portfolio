# Ввод числа
num = int(input("Введите загаданное число: "))

# 1000 отступов
number_of_characters = len(str(num))
print('—' * (number_of_characters + 26))
import time
time.sleep(2.5)
for q in range(1000):
    print()

# 10 подборов
def selection(num):
    i = int(input('Подберите число: '))
    if i == num:
        print("Вы угадали!")
        exit(num)
    else:
        if i > num:
            print("Загаданное число меньше")
        if i < num:
            print("Загаданное число больше")
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)
selection(num)

# Проигрыш
print('Вы проиграли. Загаданное число -', num)
