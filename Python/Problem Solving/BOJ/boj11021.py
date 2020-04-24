from sys import stdin

t = int(stdin.readline())

for i in range(t):
    temp = str(stdin.readline())
    a, b = temp.rstrip('\n').split()
    res = int(a) + int(b)
    print('Case #%d: %d' %(i + 1, int(res)))