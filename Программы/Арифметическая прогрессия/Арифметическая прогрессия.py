# Формула n-го члена: an = a + d · (n - 1)
print('Нахождение n-го члена геометрической прогрессии по формуле «an = a + d · (n - 1)»')
print('Введите значения переменных:')
a = int(input('a = '))
d = int(input('d = '))
n = int(input('n = '))
an = a + d * (n - 1)
print('an =', an)
