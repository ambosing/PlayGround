import string
import sys

alpha_up = list(string.ascii_uppercase)

while True:
    s = sys.stdin.readline().rstrip()
    if s[0] == "#":
        break
    result = 0
    cnt = 0
    for c in s:
        cnt += 1
        if c == " ":
            continue
        result += (alpha_up.index(c) + 1) * cnt
    sys.stdout.write(str(result) + "\n")
