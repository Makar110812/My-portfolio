# КОД ЧАСТИЧНО НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 == x2 or y1 == y2) or (abs(x1 - x2) == abs(y1 - y2)):
    print('yes')
else:
    print('no')
