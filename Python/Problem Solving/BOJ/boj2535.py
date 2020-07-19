lst = list()
num = [0] * 1000
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[2], x[1], x[0]), reverse=True)
cnt = 0
for item in lst:
    if cnt == 3:
        break
    if num[item[0]] < 2:
        print(item[0], item[1])
        cnt += 1
        num[item[0]] += 1

