from collections import defaultdict

for _ in range(int(input())):
    dic = defaultdict(int)
    for _ in range(int(input())):
        key = int(input())
        dic[key] += 1
    max_val = max(dic.values())
    dic = sorted(dic.items())
    for k, v in dic:
        if v == max_val:
            print(k)
            break

