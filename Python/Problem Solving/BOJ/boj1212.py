import sys

n = input()
lst = ["000", "001", "010", "011", "100", "101", "110", "111"]
result = ""
if n[0] == "0":
	print(0)
else:
	for i, v in enumerate(n):
		s = lst[int(v)]
		if i == 0:
			s = str(int(s))
		result += s
print(result)
