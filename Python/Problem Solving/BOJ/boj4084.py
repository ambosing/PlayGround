while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and a == b and a == c and a == d:
        break
    cnt = 0
    while a != b or b != c or c != d:
        temp1 = abs(a - b)
        temp2 = abs(b - c)
        temp3 = abs(c - d)
        temp4 = abs(d - a)
        a, b, c, d = temp1, temp2, temp3, temp4
        cnt += 1
    print(cnt)
