import string
import sys

t = int(input())
alpha = list(string.ascii_uppercase)
for i in range(t):
    a, b = map(int, input().split())
    s = list(input())
    for c in s:
        x = ord(c) - 65
        idx = (a * x + b) % 26
        sys.stdout.write(alpha[idx])
    sys.stdout.write("\n")
