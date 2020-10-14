def is_in_list(lst, item):
    if item in lst:
        return True
    else:
        return False


n, p = map(int, input().split())
a = []
while not is_in_list(a, n):
    a.append(n)
    nn = n ** 2
    pp = nn % p
    n = pp

print(len(a))
