import sys

for _ in range(int(input())):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            temp = (a ** 2 + b ** 2 + m) / (a * b)
            if temp.is_integer():
                cnt += 1
    sys.stdout.write(str(cnt) + "\n")
