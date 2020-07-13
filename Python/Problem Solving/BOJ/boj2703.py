import string
import sys

alpha_up = list(string.ascii_uppercase)

for _ in range(int(input())):
    s = input()
    rule = input()
    for c in s:
        if c == " ":
            sys.stdout.write(" ")
            continue
        idx = alpha_up.index(c)
        sys.stdout.write(rule[idx])
    print()
