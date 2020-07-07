def cmp(a, b):
    for i, v in enumerate(a):
        if not a[i]:
            return -b[i]
        if not b[i]:
            return a[i]
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])
    return 0


pre = ""
desc_chk = True
inc_chk = True
for idx in range(int(input())):
    cur = input()
    if idx == 0:
        pre = cur
        continue
    if cmp(cur, pre) > 0:
        desc_chk = False
    elif cmp(cur, pre) < 0:
        inc_chk = False
    pre = cur
if desc_chk:
    print("DECREASING")
elif inc_chk:
    print("INCREASING")
else:
    print("NEITHER")
