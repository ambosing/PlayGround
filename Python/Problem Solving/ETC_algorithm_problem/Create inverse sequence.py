n = int(input())
lst = list(map(int, input().split()))

res = [101] * n
cnt = 0
for i in lst:
    cnt += 1
    idx = 0
    cnt2 = 0
    for j in range(n):
        if cnt2 >= i:
            break
        if res[j] == 101:
            cnt2 += 1
        idx += 1
    while res[idx] != 101:
        idx += 1
    res[idx] = cnt
res = list(map(str, res))
print(' '.join(res))
