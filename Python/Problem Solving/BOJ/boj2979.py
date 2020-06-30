a, b, c = map(int, input().split())
lst = []

for _ in range(3):
    lst.append(list(map(int, input().split())))
min_val = min(lst[0][0], lst[1][0], lst[2][0])
max_val = max(lst[0][1], lst[1][1], lst[2][1])
result = 0
for i in range(min_val, max_val):
    i += 0.5
    cnt = 0
    for j in range(3):
        if lst[j][0] <= i <= lst[j][1]:
            cnt += 1
    if cnt == 1:
        result += a
    elif cnt == 2:
        result += 2 * b
    else:
        result += 3 * c
print(result)
