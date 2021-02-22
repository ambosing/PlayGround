time = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    time.append([s, e])
time.sort(key=lambda x: (x[1], x[0]))
pre = 0
cnt = 0
for s, e in time:
    if s >= pre:
        pre = e
        cnt += 1
print(cnt)

