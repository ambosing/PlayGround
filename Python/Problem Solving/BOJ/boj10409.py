n, t = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in lst:
    if t >= i:
        cnt += 1
        t -= i
    else:
        break
print(cnt)
