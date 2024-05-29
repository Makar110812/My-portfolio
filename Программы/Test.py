i_1 = int(input())
i_2 = int(input())
sign = input()
if sign == '/':
    if i_2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(i_1 / i_2)
elif sign == '*':
    print(i_1 * i_2)
elif sign == '-':
    print(i_1 - i_2)
elif sign == '+':
    print(i_1 + i_2)
else:
    print('ERROR ' * 1000000000)