n, m = map(int, input().split())

lst1 = []
lst2 = []
for i in range(n * 2):
    if i < n:
        lst1.append(input())
    else:
        lst2.append(input())
chk = True
for i in range(n):
    s = ""
    for c in lst1[i]:
        s += c * 2
    if s != lst2[i]:
        chk = False
if chk:
    print("Eyfa")
else:
    print("Not Eyfa")
