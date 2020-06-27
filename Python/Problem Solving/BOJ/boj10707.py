lst = []

for _ in range(5):
    lst.append(int(input()))

x = lst[0] * lst[4]
temp = lst[4] - lst[2] if lst[4] - lst[2] > 0 else 0
y = lst[1] + temp * lst[3]
print(min(x, y))
