lst = []

for i in range(int(input())):
    lst.append(int(input()))
if lst[1] - lst[0] == lst[2] - lst[1]:
    d = lst[1] - lst[0]
    print(lst[-1] + d)
if lst[1] ** 2 == lst[2] * lst[0]:
    if lst[0] != 0:
        r = lst[1] // lst[0]
    elif lst[1] != 0:
        r = lst[2] // lst[1]
    print(lst[-1] * r)

