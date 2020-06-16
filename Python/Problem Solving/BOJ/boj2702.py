t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    c, d = a, b
    while a > 0:
        temp = a
        a = b % a
        b = temp
    gcd = b
    lcm = (c * d) // gcd
    print(lcm, gcd)
