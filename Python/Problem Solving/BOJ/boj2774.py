t = int(input())

for i in range(t):
    num = int(input())
    cnt = 0
    lst = [0] * 10
    while num > 0:
        idx = num % 10
        if lst[idx] == 0:
            lst[idx] += 1
        num //= 10
    print(sum(lst))
