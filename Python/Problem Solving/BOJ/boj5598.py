s = input()
for c in s:
    print_c = ord(c) - 3
    if print_c < 65:
        print(chr(print_c + 26), end="")
    else:
        print(chr(print_c), end="")
