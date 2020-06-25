k = int(input())

a = 0
b = 1
len_ab = 1

if k == 1:
    print(a, b)
else:
    for _ in range(1, k):
        a = b
        b = len_ab
        len_ab = a + b
    print(a, b)
