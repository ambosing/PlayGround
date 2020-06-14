import string

s = input()
alpha_low = list(string.ascii_lowercase)
alpha_up = list(string.ascii_uppercase)

for c in s:
    if c in alpha_low:
        idx = (alpha_low.index(c) + 13) % 26
        print_c = alpha_low[idx]
    elif c in alpha_up:
        idx = (alpha_up.index(c) + 13) % 26
        print_c = alpha_up[idx]
    else:
        print_c = c
    print(print_c, end="")

