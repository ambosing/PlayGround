from itertools import combinations


lst = []
while True:
    s = input().split()
    lst.append(s)
    if s[0] == "0":
        break

for i, line in enumerate(lst):
    k, *lst = line
    k = int(k)
    if k == 0:
        break
    for item in (combinations(lst, 6)):
        item = list(item)
        print(' '.join(item))
    if lst[i + 1][0] == "0":
        break
    print()
