'''
n = int(input())
time = [0] * 3
cnt = 0
lim = (n + 1) * 3600 - 1
for i in range(lim):
    s = i % 60
    m = i % 3600 // 60
    h = i // 3600
    if s // 10 == 3 or s % 10 == 3 or m // 10 == 3 or m % 10 == 3 or h // 10 == 3 or h % 10 == 3:
        cnt += 1
print(cnt)
'''

n = int(input())
res = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                res += 1
print(res)
