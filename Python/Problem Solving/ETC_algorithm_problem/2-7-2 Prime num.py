n = int(input())
prime = [True] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if not prime[i]:
        continue
    cnt += 1
    for j in range(i + i, n + 1, i):
        if prime[j]:
            prime[j] = False
print(cnt)
