from collections import defaultdict


dic = [defaultdict(int) for _ in range(2)]
key = []
for i in range(2):
    s = input()
    for c in s:
        dic[i][c] += 1
    key.extend(set(s))
res = 0

for k in set(key):
    if k not in dic[1]:
        res += dic[1][k]
        res += dic[0][k]
    else:
        res += abs(dic[1][k] - dic[0][k])
print(res)
