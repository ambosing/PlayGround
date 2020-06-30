lst = [i + 1 for i in range(3)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    lst[a - 1], lst[b - 1] = lst[b - 1], lst[a - 1]
print(lst.index(1) + 1)