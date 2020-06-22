import string

alpha_low = list(string.ascii_lowercase)
t = int(input())

for i in range(t):
    s = input().lower()
    lst = [0] * 26
    for c in s:
        if c == '.' or c == ',' or c == '?' or c == '!' or c == '"' or c == "'" or c == " " or c.isdigit():
            continue
        idx = alpha_low.index(c)
        if lst[idx] == 0:
            lst[idx] += 1
    if sum(lst) == 26:
        print("pangram")
    else:
        print("missing", end=" ")
        for j in range(len(lst)):
            if lst[j] == 0:
                print(alpha_low[j], end="")
        print()