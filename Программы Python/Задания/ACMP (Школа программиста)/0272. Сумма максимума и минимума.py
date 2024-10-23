maximum = []
minimum = []
i = list(map(int, input().split()))
for n in range(1, (len(i) + 1)):
    if n % 2 == 0:
        maximum.append(i[n - 1])
    else:
        minimum.append(i[n - 1])
output = max(maximum) + min(minimum)
print(output)
