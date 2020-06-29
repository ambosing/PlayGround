a, b = map(int, input().split())
lst_len = 0
lst = []
cnt = 1
result = 0

while True:
    if lst_len >= 1000:
        break
    for i in range(cnt):
        lst.append(cnt)
        lst_len += 1
    cnt += 1

for i in range(a - 1, b):
    result += lst[i]
print(result)
