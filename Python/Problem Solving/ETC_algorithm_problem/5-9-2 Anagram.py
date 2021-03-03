from collections import defaultdict

s1 = input()
s2 = input()
dic1 = defaultdict(int)
dic2 = defaultdict(int)
for c in s1:
    dic1[c] += 1
for c in s2:
    dic2[c] += 1
for k, v in dic1.items():
    if k not in dic2 or v != dic2[k]:
        print("NO")
        break
else:
    print("YES")
