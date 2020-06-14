import sys

n, m = input().split()
cnt = 0
lst = list(n)
m = int(m)
chk = False

n = int(n)
for i in range(n):
    for j in lst:
        sys.stdout.write(str(j))
        cnt += 1
        if cnt == m:
            chk = True
            break
    if chk:
        break
