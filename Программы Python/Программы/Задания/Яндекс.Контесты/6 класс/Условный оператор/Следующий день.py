# КОД ЧАСТИЧНО НЕ ПРОШЁЛ ПРОВЕРКУ! Возможны ошибки.

day, mouth, year = int(input()), int(input()), int(input())

visokosny = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

new_day = day
new_mouth = mouth
new_year = year

if mouth == 1 or mouth == 3 or mouth == 5 or mouth == 7 or mouth == 8 or mouth == 10 or mouth == 12:
    if day == 31:
        new_day = 1
        new_mouth = mouth + 1
    else:
        new_day = day + 1

    if mouth == 13:
        new_mouth = 1
        new_year = year + 1


if mouth == 4 or mouth == 6 or mouth == 9 or mouth == 11:
    if day == 30:
        new_day = 1
        new_mouth = mouth + 1
    else:
        new_day = day + 1

if mouth == 2:
    if visokosny:
        if day == 29:
            new_day = 1
            new_mouth = mouth + 1
        else:
            new_day = day + 1
    else:
        if day == 28:
            new_day = 1
            new_mouth = mouth + 1
        else:
            new_day = day + 1

print(f'{new_day}.{new_mouth}.{new_year}')
