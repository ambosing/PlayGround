n = int(input())
m = int(input())

i = 1
ii = 1
lst = []
while ii <= m:
    if n <= ii <= m:
        lst.append(ii)
    i += 1
    ii = i * i


if len(lst) > 0:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
