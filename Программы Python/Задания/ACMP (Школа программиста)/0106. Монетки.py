listt = []
one = zero = 0
for _ in range(int(input())):
    n = int(input())
    listt += [n]
    if n == 1:
        one += 1
    else:
        zero += 1
if one == zero:
    print(one)
elif one > zero:
    print(zero)
else:
    print(one)