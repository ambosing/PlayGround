n = int(input())

cnt = 0
for i in range(1, 500):
    b = i ** 2
    for j in range(i + 1, 500):
        a = j ** 2
        if a == b + n:
            cnt += 1
        elif a > b + n:
            break
print(cnt)
