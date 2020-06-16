lst = [0] * 30

for i in range(28):
    idx = int(input()) - 1
    lst[idx] = 1

for i in range(30):
    if lst[i] == 0:
        print(i + 1)
