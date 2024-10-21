a_1, a_2 = map(int, input().split())
b_1, b_2 = map(int, input().split())
c_1, c_2 = map(int, input().split())
d_1, d_2 = map(int, input().split())
r_1 = a_1 - a_2
r_2 = b_1 - b_2
r_3 = c_1 - c_2
r_4 = d_1 - d_2
r = r_1 + r_2 + r_3 + r_4
if r > 0:
    print(f"1")
elif r < 0:
    print(f"2")
else:
    print(f"DRAW")