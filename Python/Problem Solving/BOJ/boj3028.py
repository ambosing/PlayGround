lst = [1, 0, 0]
s = list(input())

for c in s:
    if c == "A":
        lst[0], lst[1] = lst[1], lst[0]
    elif c == "B":
        lst[1], lst[2] = lst[2], lst[1]
    else:
        lst[0], lst[2] = lst[2], lst[0]
print(lst.index(1) + 1)
