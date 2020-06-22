import string

alpha_low = string.ascii_lowercase
alpha_sum = 0

for i in alpha_low:
    alpha_sum += ord(i)

while True:
    s = input()
    if s.count("*") > 0:
        break
    lst = []
    lst_sum = 0
    for c in s:
        chk = True
        if c == " ":
            continue
        for i in lst:
            if i == c:
                chk = False
        if chk:
            lst.append(c)
    for i in lst:
        lst_sum += ord(i)
    if lst_sum == alpha_sum:
        print("Y")
    else:
        print("N")