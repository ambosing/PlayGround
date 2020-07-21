n = int(input())
f = int(input())
n //= 100
n *= 100
min_val = 100
for _ in range(100):
    if n % f == 0:
        temp = n % 100
        if min_val > temp:
            min_val = temp
    n += 1
print("%02d" % min_val)
