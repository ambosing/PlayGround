n = int(input())

i = 0
while n > 0:
    if n >= 3:
        n -= 3
    else:
        n -= 1
    i += 1
if i % 2 == 0:
    print("SK")
else:
    print("CY")
