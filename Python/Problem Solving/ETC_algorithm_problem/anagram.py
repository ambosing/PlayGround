from collections import defaultdict

dic1 = defaultdict(int)
dic2 = defaultdict(int)

s1 = input()
s2 = input()

for c in s1:
    dic1[c] += 1
for c in s2:
    dic2[c] += 1

for k in dic1.keys():
    if dic1[k] != dic2[k]:
        print("NO")
        break
else:
    print("YES")
