from collections import defaultdict


def is_in_list(lst, item):
    if item in lst:
        return True
    else:
        return False


n, p = map(int, input().split())
dic = defaultdict(int)
a = []
num = n
dic[num] = 0
while max(dic.values()) < 3:
    dic[num] += 1
    nn = num * n
    num = nn % p

res = 0
for k, v in dic.items():
    if v >= 2:
        res += 1
print(res)
