lst = list(map(int, input().split()))
s = input()
a = min(lst)
d = max(lst)
b = 0
cnt = 0
for i in lst:
    if i != a and i != d:
        b = i
for c in s:
    if c == "A":
        print(a, end="")
    elif c == "B":
        print(b, end="")
    elif c == "C":
        print(d, end="")
    cnt += 1
    if cnt != 3:
        print(end=" ")
