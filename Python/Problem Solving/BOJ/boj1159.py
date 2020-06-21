import string

alpha_low = string.ascii_lowercase
dic = dict()
n = int(input())
lst = []

for i in alpha_low:
    dic[i] = 0

for i in range(n):
    key = input()[0]
    dic[key] += 1

for key in dic.keys():
    if dic[key] >= 5:
        lst.append(key)
lst.sort()
if lst:
    print(''.join(lst))
else:
    print("PREDAJA")
