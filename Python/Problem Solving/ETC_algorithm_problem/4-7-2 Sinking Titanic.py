n, m = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
lt = 0
rt = n - 1
res = 0
while lt <= rt:
    if p[lt] + p[rt] > m:
        res += 1
        rt -= 1
    else:
        lt += 1
        rt -= 1
        res += 1
print(res)
