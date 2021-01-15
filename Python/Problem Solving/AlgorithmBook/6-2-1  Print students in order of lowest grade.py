n = int(input())
lst = []
for _ in range(n):
    a, b = input().split()
    lst.append([a, int(b)])
lst.sort(key=lambda x: x[1])

for i, v in enumerate(lst):
    if i != len(lst) - 1:
        print(v[0], end=" ")
    else:
        print(v[0], end="")
