banned_list = ["False", "True", "None", "and", "with", "as", "assert", "break", "class", "contune", "def", "del", "elif", "else", "expert", "finaly", "try", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "while", "yield"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
n = input()
if (n not in banned_list) and (n[0] not in numbers):
    print(f"Это имя переменной возможно.")
else:
    print(f"Это имя переменной невозможно.")