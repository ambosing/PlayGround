from functools import cmp_to_key


def cmp(a, b):
    for i, v in enumerate(a):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])
    return 0


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def permutation(res, lst, n_, k_, d):
    if d == k_:
        res.append(' '.join(lst))
    else:
        for i in range(d, n_):
            swap(lst, i, d)
            permutation(res, lst, n, k_, d + 1)
            swap(lst, i, d)


n = int(input())
lst_val = [str(i + 1) for i in range(n)]
result = list()
permutation(result, lst_val, n, n, 0)
result = sorted(result, key=cmp_to_key(cmp))
print('\n'.join(result))
