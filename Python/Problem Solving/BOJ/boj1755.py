from collections import OrderedDict

num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
a, b = map(int, input().split())
dic = dict()
num_lst = [i for i in range(a, b + 1)]

for i in num_lst:
    s = str()
    val = i
    i = str(i)
    i = int(i[::-1])
    while i > 0:
        idx = (i % 10)
        s += num[idx]
        i //= 10
    if val % 10 == 0:
        s += "zero"
    dic[s] = val
ordered_dict = OrderedDict(sorted(dic.items(), key=lambda t:t[0]))
cnt = 0
for i in ordered_dict.values():
    cnt += 1
    if cnt % 10 == 0:
        print(i)
    else:
        print(i, end=" ")
