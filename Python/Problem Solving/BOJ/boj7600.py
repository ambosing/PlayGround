import string

alpha_low = list(string.ascii_lowercase)

while True:
    s = input().lower()
    lst = [0] * 26
    if s[0] == "#":
        break
    for c in s:
        if c.isalpha():
            idx = alpha_low.index(c)
            if lst[idx] == 0:
                lst[idx] += 1
    print(sum(lst))
