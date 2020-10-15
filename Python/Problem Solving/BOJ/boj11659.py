import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
hap_lst = [0]
hap = 0
for i in a:
    hap += i
    hap_lst.append(hap)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(hap_lst[e] - hap_lst[s-1]) + "\n")

