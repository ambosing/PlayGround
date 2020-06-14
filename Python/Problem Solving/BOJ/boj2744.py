s = input()
len_s = len(s)

for i in range(len_s):
    if s[i].islower():
        print(chr(ord(s[i]) - 32), end="")
    else:
        print(chr(ord(s[i]) + 32), end="")
