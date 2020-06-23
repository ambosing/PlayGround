import string

alpha_low = list(string.ascii_lowercase)
cnt = 0
while True:
    s1 = input()
    s2 = input()
    chk = True
    cnt += 1
    if s1 == "END" and s2 == "END":
        break
    lst = [0] * 26
    lst2 = [0] * 26
    for c in s1:
        idx = alpha_low.index(c)
        lst[idx] += 1
    for c in s2:
        idx = alpha_low.index(c)
        lst2[idx] += 1
    for i in range(26):
        if lst[i] != lst2[i]:
            chk = False
            break
    if chk:
        print("Case %d: same" % cnt)
    else:
        print("Case %d: different" % cnt)
