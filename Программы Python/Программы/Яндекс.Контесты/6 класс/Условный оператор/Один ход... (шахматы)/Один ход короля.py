# КОД НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if ((abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)) or ((abs(x1 - x1) == abs(y1 - y2)) and abs(x1 - x1) == 1):
    print('yes')
else:
    print('no')