def factorial(s, e):
    if s == e:
        return 1
    return_div = s
    for val in range(s - 1, e, -1):
        return_div *= val
    return return_div


n, k = map(int, input().split())
nk = n - k
if n == k:
    result = 1
elif nk < k:
    div = factorial(nk, 0)
    dived = factorial(n, k)
    result = dived // div
else:
    div = factorial(k, 0)
    dived = factorial(n, nk)
    result = dived // div
print(result)
