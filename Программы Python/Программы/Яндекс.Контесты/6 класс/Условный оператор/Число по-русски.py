# ЭТОТ КОД НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

number = int(input('Введите число:'))

number_len = len(str(number))


while number >= 10:
    number_1 = number // 10
while number >= 100:
    number_2 = number // 100
while number >= 1000:
    number_3 = number // 1000


nado = True


if number_len == 1:
    if number == 1:
        print(f'один')
    elif number == 2:
        print(f'два')
    elif number == 3:
        print(f'три')
    elif number == 4:
        print(f'четыре')
    elif number == 5:
        print(f'пять')
    elif number == 6:
        print(f'шесть')
    elif number == 7:
        print(f'семь')
    elif number == 8:
        print(f'восемь')
    elif number == 9:
        print(f'девять')


if number_len == 2:

    if number_2 == 1:
        if number == 10:
            str_number_2 = 'десять'
        if number == 11:
            str_number_2 = 'одиннадцать'
        if number == 12:
            str_number_2 = 'двенадцать'
        if number == 13:
            str_number_2 = 'тринадцать'
        if number == 14:
            str_number_2 = 'четырнадцать'
        if number == 15:
            str_number_2 = 'пятнадцать'
        if number == 16:
            str_number_2 = 'шестнадцать'
        if number == 17:
            str_number_2 = 'семнадцать'
        if number == 18:
            str_number_2 = 'восемнадцать'
        if number == 19:
            str_number_2 = 'девятнадцать'
        print(f'{str_number_2}')
    
    else:

        if number_1 == 1:
            str_number_1 = 'один'
        elif number == 2:
            str_number_1 = 'два'
        elif number == 3:
            str_number_1 = 'три'
        elif number == 4:
            str_number_1 = 'четыре'
        elif number == 5:
            str_number_1 = 'пять'
        elif number == 6:
            str_number_1 = 'шесть'
        elif number == 7:
            str_number_1 = 'семь'
        elif number == 8:
            str_number_1 = 'восемь'
        elif number == 9:
            str_number_1 = 'девять'

        if number == 2:
            str_number_2 = 'двадцать'
        elif number == 3:
            str_number_2 = 'тридцать'
        elif number == 4:
            str_number_2 = 'сорок'
        elif number == 5:
            str_number_2 = 'пятьдесят'
        elif number == 6:
            str_number_2 = 'шестьдесят'
        elif number == 7:
            str_number_2 = 'семьдесят'
        elif number == 8:
            str_number_2 = 'восемьдесят'
        elif number == 9:
            str_number_2 = 'девяносто'

        print(f'{str_number_2} {str_number_1}')

if number_len == 3:

    if number_2 == 1:
        if number == 10:
            str_number_2 = 'десять'
        if number == 11:
            str_number_2 = 'одиннадцать'
        if number == 12:
            str_number_2 = 'двенадцать'
        if number == 13:
            str_number_2 = 'тринадцать'
        if number == 14:
            str_number_2 = 'четырнадцать'
        if number == 15:
            str_number_2 = 'пятнадцать'
        if number == 16:
            str_number_2 = 'шестнадцать'
        if number == 17:
            str_number_2 = 'семнадцать'
        if number == 18:
            str_number_2 = 'восемнадцать'
        if number == 19:
            str_number_2 = 'девятнадцать'
        nado = False
    
    else:

        if number_1 == 1:
            str_number_1 = 'один'
        elif number == 2:
          str_number_1 = 'два'
        elif number == 3:
            str_number_1 = 'три'
        elif number == 4:
            str_number_1 = 'четыре'
        elif number == 5:
            str_number_1 = 'пять'
        elif number == 6:
            str_number_1 = 'шесть'
        elif number == 7:
            str_number_1 = 'семь'
        elif number == 8:
            str_number_1 = 'восемь'
        elif number == 9:
            str_number_1 = 'девять'

        if number == 2:
            str_number_2 = 'двадцать'
        elif number == 3:
            str_number_2 = 'тридцать'
        elif number == 4:
            str_number_2 = 'сорок'
        elif number == 5:
            str_number_2 = 'пятьдесят'
        elif number == 6:
            str_number_2 = 'шестьдесят'
        elif number == 7:
            str_number_2 = 'семьдесят'
        elif number == 8:
            str_number_2 = 'восемьдесят'
        elif number == 9:
            str_number_2 = 'девяносто'

    if nado:
        print(f'{str_number_3} {str_number_2} {str_number_1}')
    else:
        print(f'{str_number_3} {str_number_2}')
