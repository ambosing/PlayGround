lst = list(map(int, input().split()))

lst.remove(max(lst))
lst.remove(min(lst))
print(lst[0])