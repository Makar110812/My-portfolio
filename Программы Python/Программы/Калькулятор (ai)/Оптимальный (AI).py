# Проведение операции сложения
def add(x, y):
    return x + y

# Проведение операции вычитания
def subtract(x, y):
    return x - y

# Проведение операции умножения
def multiply(x, y):
    return x * y

# Проведение операции деления
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! На 0 делить нельзя."

# Выбор операции
print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

# Ввод операции
choice = input("Введите номер операции (1/2/3/4): ")

# Ввод переменных
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Проверка кода операции
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Некорректный ввод")
