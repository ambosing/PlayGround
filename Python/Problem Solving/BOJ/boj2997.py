lst = list(map(int, input().split()))
lst.sort()
d1 = lst[1] - lst[0]
d2 = lst[2] - lst[1]
if d2 > d1:
    print(lst[1] + d1)
elif d2 < d1:
    print(lst[0] + d2)
else:
    print(lst[2] + d2)
