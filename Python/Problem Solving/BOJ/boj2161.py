n = int(input())
lst = [i + 1 for i in range(n)]
for i in range(n):
    print(lst.pop(0), end="")
    if i + 1 != n:
        print(end=" ")
        lst.append(lst.pop(0))