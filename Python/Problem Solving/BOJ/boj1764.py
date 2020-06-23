import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
result = []
res_cnt = 0
for _ in range(a + b):
    s = sys.stdin.readline().rstrip()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 0

for k, v in dic.items():
    if v >= 1:
        result.append(k)
        res_cnt += 1
result.sort()
print(res_cnt)
print("\n".join(result))
