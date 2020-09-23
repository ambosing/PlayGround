def gcd(g, g2):
    while g2 > 0:
        temp = g % g2
        g = g2
        g2 = temp
    return g


a, b = map(int, input().split())
c, d = map(int, input().split())
gd = gcd(b, d)
lcm = (b * d) // gd
num = (lcm // b) * a + (lcm // d) * c
gd2 = gcd(lcm, num)
print(num // gd2, lcm // gd2)
