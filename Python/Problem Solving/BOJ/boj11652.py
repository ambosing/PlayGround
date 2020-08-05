dic = dict()
for _ in range(int(input())):
    n = int(input())
    if n not in dic:
        dic[n] = 0
    else:
        dic[n] += 1

max_val = max(dic.values())
dic = sorted(dic.items())

for k, v in dic:
    if v == max_val:
        print(k)
        break
