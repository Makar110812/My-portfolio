# КОД НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

# ax² + bx + c = 0

a, b, c = int(input()), int(input()), int(input())

import math
D = b ** 2 - 4 * a * c
print(D)
if D < 0:
    print("no solutions")
elif D == 0:
    x = -b / 2 * a
    print (x)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1)
    print(x2)
