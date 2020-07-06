import sys

n = input()
len_n = len(n)
lst = []

if len_n % 3 == 1:
	n = "00" + n
	len_n += 2
elif len_n % 3 == 2:
	n = "0" + n
	len_n += 1

for i in range(len_n - 1, 0, -3):
	num = int(n[i])
	num += int(n[i - 1]) * 2
	num += int(n[i - 2]) * 4
	lst.append(str(num))
lst = lst[::-1]
print(''.join(lst))
