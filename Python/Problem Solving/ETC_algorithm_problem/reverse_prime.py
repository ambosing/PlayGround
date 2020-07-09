def reverse(x):
    x = x[::-1]
    return int(x)


def is_prime(x):
    ii = 2
    if x < 2:
        return 0
    while ii <= x // ii:
        if x % ii == 0:
            return 0
        ii += 1
    return 1


n = int(input())
lst = list(input().split())
res = list()

for i in range(n):
    num = reverse(lst[i])
    if is_prime(num):
        res.append(str(num))
print(' '.join(res))
