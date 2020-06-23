lst = []
t = int(input())

for _ in range(t):
    lst.append(input())
mode = int(input())

for i in range(t):
    if mode == 1:
        print(lst[i])
    elif mode == 2:
        s = lst[i]
        s = s[::-1]
        print(s)
    else:
        print(lst[t - i - 1])
