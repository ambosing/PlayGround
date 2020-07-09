n = int(input())
is_prime = [True] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if is_prime[i]:
        cnt += 1
        for j in range(i + i, n + 1, i):
            is_prime[j] = False
print(cnt)
