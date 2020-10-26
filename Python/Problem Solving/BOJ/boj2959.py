lst = list(map(int, input().split()))

lst.sort()
res = min(lst[0], lst[1]) * min(lst[2], lst[3])
print(res)
