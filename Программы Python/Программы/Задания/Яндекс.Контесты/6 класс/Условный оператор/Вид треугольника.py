a, b, c = int(input()), int(input()), int(input())

if (a <= (b + c)) and (b <= (a + c)) and (c <= (b + a)):
    print('yes')
    
    if c ** 2 > a ** 2 + b ** 2 or b ** 2 > c ** 2 + a ** 2 or a ** 2 > c ** 2 + b ** 2:
        print('obtuse')
    elif c ** 2 == a ** 2 + b ** 2 or b ** 2 == c ** 2 + a ** 2 or a ** 2 == c ** 2 + b ** 2:
        print('rectangular')
    elif c ** 2 < a ** 2 + b ** 2 or b ** 2 < c ** 2 + a ** 2 or a ** 2 < c ** 2 + b ** 2:
        print('acute-angled')

else:
    print('no')