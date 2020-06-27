import string

alpha_up = list(string.ascii_uppercase)
t = int(input())
for i in range(t):
    s = input()
    print("String #%d" % (i + 1))
    for c in s:
        idx = (alpha_up.index(c) + 1) % 26
        print(alpha_up[idx], end="")
    if i + 1 != t:
        print("\n")
