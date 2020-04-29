x = list()
y = list()

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) != 2:
        print(x[i], end=' ')

for i in range(3):
    if y.count(y[i]) != 2:
        print(y[i])
