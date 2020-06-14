a, b = map(int, input().split())
lst = []

limit = 1
cnt = 0
while True:
    for j in range(limit):
        lst.append(limit)
        cnt += 1
    if cnt > 1000:
        break
    limit += 1

result = 0
for i in range(a, b + 1):
    result += lst[i - 1]
print(result)
