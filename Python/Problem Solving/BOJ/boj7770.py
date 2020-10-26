n = int(input())
t = 1
i = 0
a = t
cnt = 0
if n == 1:
    print(1)
else:
    while n >= a:
        i += 4
        t += i
        cnt += 1
        a += t
    print(cnt)
