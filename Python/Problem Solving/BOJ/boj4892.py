i = 0
while True:
    i += 1
    num = int(input())
    if num == 0:
        break
    num = 3 * num
    if num % 2 == 0:
        num = num // 2
        s = "even"
    else:
        num = (num + 1) // 2
        s = "odd"
    num //= 3
    if s == "even":
        print("%d. even %d" % (i, num))
    else:
        print("%d. odd %d" % (i, num))