lst = []
m = list(map(int, input().split()))
n = list(map(int, input().split()))

lst.append(sum(m))
lst.append((sum(n)))
print(max(lst))
