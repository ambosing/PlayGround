m = int(input())
n = int(input())

num = 1
i = 2
lst = list()
while num <= n:
    if m <= num <= n:
        lst.append(num)
    num = i ** 2
    i += 1

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
