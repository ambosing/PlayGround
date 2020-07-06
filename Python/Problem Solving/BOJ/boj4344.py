import sys

for _ in range(int(input())):
	lst = list(map(int, sys.stdin.readline().rstrip().split()))
	hap = sum(lst) - lst[0]
	avg = hap // lst[0]
	cnt = 0
	for i, v in enumerate(lst):
		if i == 0:
			continue
		if v > avg:
			cnt += 1
	print("%.3f%%" % ((cnt / lst[0]) * 100))