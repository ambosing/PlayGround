from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n * 2 - 1):
    s = input()
    dic[s] += 1

for k, v in dic.items():
    if v == 1:
        print(k)
        break
