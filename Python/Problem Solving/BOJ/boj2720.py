t = int(input())

coin = [25, 10, 5, 1]

for i in range(t):
    price = int(input())
    lst = ['0'] * 4
    idx = 0
    while price > 0:
        lst[idx] = str(price // coin[idx])
        price = price % coin[idx]
        idx += 1
    print(' '.join(lst))
