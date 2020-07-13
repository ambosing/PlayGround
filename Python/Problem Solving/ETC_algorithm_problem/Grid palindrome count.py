lst = []

for i in range(7):
    lst.append(list(input().split()))

cnt = 0
for i in range(7):
    for j in range(3):
        s = lst[i]
        s = s[j:j + 5]
        if s == s[::-1]:
            cnt += 1
        for k in range(2):
            if lst[j][i] == lst[5 - k + j][i]:
                break
    else:
         cnt += 1
print(cnt)
