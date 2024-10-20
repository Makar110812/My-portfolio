# Ввод оценки по 10-бальной шкале
evaluation_10marks = int(input('Оценка по 10-бальной шкале | '))

# Перевод оценки в 5-бальную шкалу и проверка ввода на подленность
if 10 >= evaluation_10marks >= 0:
    if evaluation_10marks >= 9:
        evaluation_5marks = 5
    elif evaluation_10marks >= 7:
        evaluation_5marks = 4
    elif evaluation_10marks >= 5:
        evaluation_5marks = 3
    elif evaluation_10marks >= 3:
        evaluation_5marks = 2
    elif evaluation_10marks != 0:
        evaluation_5marks = 1
    else:
        evaluation_5marks = 0
else:
    print('_________________________________________________________________')
    print('Ошибка: введено неправильное значение оценки по 10-бальной шкале.')
    stop()

# Вывод оценки по 5-бальной шкале
print('Оценка по 5-бальной шкале  |', evaluation_5marks)
