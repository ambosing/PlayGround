n = int(input())
cnt = 0
for i in range(3600 * (n + 1)):
    h = str(i // 3600)
    m = str(i % 3600 // 60)
    s = str(i % 60)
    if '3' in h + m + s:
        cnt += 1
print(cnt)
