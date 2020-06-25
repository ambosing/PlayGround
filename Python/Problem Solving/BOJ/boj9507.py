lst = [0, 1, 1, 2]

for i in range(4, 69):
    lst.append(lst[i - 1] + lst[i - 2] + lst[i - 3] + lst[i - 4])

for _ in range(int(input())):
    n = int(input())
    if n < 2:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        print(lst[n + 1])