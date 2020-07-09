t = int(input())

for i in range(t):
    h = int(input())
    s = input()
    for c in s:
        if c == "c":
            h += 1
        else:
            h -= 1
    print("Data Set %d:\n%d" % (i + 1, h))
    if i != t - 1:
        print()
