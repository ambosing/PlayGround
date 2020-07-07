n = int(input())
cnt = 0

while n > 0:
    if n > 3:
        cnt = n // 3
        n %= 3
        continue
    else:
        n -= 1
    cnt += 1
if cnt % 2 == 1:
    print("SK")
else:
    print("CY")
