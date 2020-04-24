n = int(input())

lst = []

while n != 1:
    m = 2
    while m != n:
        if n % m == 0:
            break
        m += 1
    n = n // m
    lst.append(m)
lst.sort()
for i in lst:
    print(i)
