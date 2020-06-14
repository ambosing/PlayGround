import string

alpha = string.ascii_uppercase
s = input().upper()
dic = dict()

for c in alpha:
    dic[c] = 0

for c in s:
    dic[c] += 1

max_val = max(dic.values())
cnt = 0
max_key = ''
for c in alpha:
    if max_val == dic[c]:
        cnt += 1
        max_key = c
if cnt >= 2:
    print("?")
else:
    print(max_key)
