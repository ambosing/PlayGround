import sys


lst = list(map(int, input().split()))
res = sys.maxsize

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            a, b, c = lst[i], lst[j], lst[k]
            while b > 0:
                temp = b
                b = a % b
                a = temp
            lcm1 = (lst[i] * lst[j]) // a
            d = lcm1
            while c > 0:
                temp = c
                c = d % c
                d = temp
            lcm2 = (lcm1 * lst[k]) // d
            if lcm2 < res:
                res = lcm2
print(res)
