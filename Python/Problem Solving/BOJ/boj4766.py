pre = -100
while True:
    cur = float(input())
    if cur == 999:
        break
    if pre != -100:
        print("%0.2f" % (cur - pre))
    pre = cur
