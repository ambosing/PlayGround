result = []

s, s2 = input().split()
len_s = len(s)
len_s2 = len(s2)
big = len_s if len_s > len_s2 else len_s2
small = len_s2 if len_s > len_s2 else len_s
s = s[::-1]
s2 = s2[::-1]
for i in range(big):
    if len_s <= i:
        result.append(s2[i])
    elif len_s2 <= i:
        result.append(s[i])
    else:
        result.append(str(int(s[i]) + int(s2[i])))
print(''.join(result[::-1]))
