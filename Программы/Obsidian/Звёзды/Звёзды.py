a, b = map(int, input().split())
print('![[Заполненная звезда.png|20]] ' * a, '![[Незаполненная звезда.png|20]] ' * (b - a), sep='')
