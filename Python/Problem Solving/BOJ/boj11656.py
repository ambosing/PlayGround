s = input()
len_s = len(s)
lst = []
for i in range(len_s):
    temp = s[i:]
    lst.append(temp)
lst.sort()
for i in lst:
    print(i)
