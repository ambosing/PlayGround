from collections import defaultdict

n = int(input())
words = defaultdict(int)
res = ""
for i in range(n * 2 - 1):
    s = input()
    words[s] += 1

for k, v in words.items():
    if v == 1:
        res = k
print(res)
