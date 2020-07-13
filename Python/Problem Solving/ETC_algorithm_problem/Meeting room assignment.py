n = int(input())
lst = list()
for _ in range(n):
    s, e = map(int, input().split())
    lst.append([s, e])
lst.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0

for s, e in lst:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
