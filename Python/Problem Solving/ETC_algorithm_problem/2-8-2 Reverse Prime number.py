def reverse(x):
    rev_lst = []
    for item in x:
        rev_lst.append(item[::-1])
    rev_lst = list(map(int, rev_lst))
    return rev_lst


def is_prime(x):
    if prime[x]:
        return True
    else:
        return False


n = int(input())
lst = list(input().split())
lst = reverse(lst)
max_val = max(lst)
prime = [True] * (max_val + 1)
prime[1] = False
res = []
for i in range(2, max_val + 1):
    if not prime[i]:
        continue
    for j in range(i + i, max_val + 1, i):
        if prime[j]:
            prime[j] = False

for i in lst:
    if is_prime(i):
        res.append(str(i))
print(' '.join(res))

