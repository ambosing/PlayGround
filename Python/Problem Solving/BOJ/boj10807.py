n = int(input())
lst = map(int, input().split())

target = int(input())
cnt = 0
for i in lst:
    if i == target:
        cnt += 1
print(cnt)
