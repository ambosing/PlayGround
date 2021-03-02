s = input()
lst = []
res = 0
for c in s:
    if not lst or c == '(':
        lst.append(c)
    else:
        lst.pop()
        if pre == '(':
            res += len(lst)
        else:
            res += 1
    pre = c
print(res)
