# КОД НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

number = int(input())
number_1 = number % 10
if number_1 == 1:
    utug = 'утюг'
elif 2 >= number_1 >= 4:
    utug = 'утюга'
elif 5 >= number_1 >= 10:
    utug = 'утюгов'
print(number, utug)