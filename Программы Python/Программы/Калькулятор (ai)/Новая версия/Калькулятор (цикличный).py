# Отступы
def indent(n):
    for _ in range(n + 1):
        print()

# Ошибка
def error(n):
    if n == 1:
        print(f"Ошибка: первое значение - не число.")
    elif n == 2:
        print(f"Ошибка: второе значение - не число.")
    elif n == 3:
        print(f"Ошибка: введён неверный знак.")
    elif n == 4:
        print(f"Ошибка: на ноль делить нельзя.")
    elif n == 5:
        print(f"Ошибка: не распознан символ.")
    elif n == 6:
        print(f"Ошибка: неверное выражение. Доступные варианты: Yes/No.")
    elif n == 7:
        print(f"Ошибка: для целочисленного деления числа должны быть целыми.")
    else:
        print(f"Ошибка: внутренняя ошибка кода. Обратитесь к разработчику.")

# Помощь
def help():
    print(f"ПОМОЩЬ\nДля того, чтобы использовать калькулятор, введите выражение следующего формата:\n<Число_1> <Символ (+; -; *; /; ^; **; //; %)> <Число_2>")

# Проверка на требование помощи
print(f"Вам нужна помощь?")
match input():
    case "True" | "y" | "Y" | "yes" | "Yes" | "YES" | "д" | "Д" | "да" | "Да" | "ДА":
        help()
        indent(1)
    case "False" | "n" | "N" | "no" | "No" | "NO" | "н" | "Н" | "нет" | "Нет" | "НЕТ":
        indent(1)
    case _:
        error(6)

while True:
    # Ввод данных
    i_1, s, i_2 = input().split()
    indent(1)

    # Проверка введённых данных
    if "." in  i_1:
        try:
            a = float(i_1)
        except ValueError:
            error(1)
        else:
            i_1 = float(i_1)
    else:
        try:
            a = int(i_1)
        except ValueError:
            error(1)
        else:
            i_1 = int(i_1)

    if "." in  i_2:
        try:
            a = float(i_2)
        except ValueError:
            error(2)
        else:
            i_2 = float(i_2)
    else:
        try:
            a = int(i_2)
        except ValueError:
            error(2)
        else:
            i_2 = int(i_2)

    if s not in ["+", "-", "*", "/", "^", "**", "//", "%"]:
        error(3)

    # Сложение
    if s == "+":
        print(f"{i_1} + {i_2} = {i_1 + i_2}")

    # Вычитание
    elif s == "-":
        print(f"{i_1} - {i_2} = {i_1 - i_2}")

    # Умножение
    elif s == "*":
        print(f"{i_1} * {i_2} = {i_1 * i_2}")

    # Разность
    elif s == "/":
        if i_2 == 0:
            error(4)
        if i_1 / i_2 == float(i_1 // i_2):
            print(f"{i_1} / {i_2} = {i_1 // i_2}")
        else:
            print(f"{i_1} / {i_2} = {i_1 / i_2}")

    # Возведение в степень
    elif s in ["^", "**"]:
        print(f"{i_1} ^ {i_2} = {i_1 ** i_2}")

    # Целочисленное деление
    elif s == "//":
        if float(int(float(i_1))) == float(i_1) and float(int(float(i_2))) == float(i_2):
            print(f"{i_1} // {i_2} = {i_1 // i_2}")
        else:
            error(7)

    # Остаток
    elif s == "%":
        print(f"{i_1} % {i_2} = {i_1 % i_2}")

    else:
        error(5)
    indent(3)
