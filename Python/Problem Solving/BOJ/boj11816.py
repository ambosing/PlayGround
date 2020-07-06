import sys
import string

n = input()
result = 0
alpha_low = list(string.ascii_lowercase)
if n.count("0x") > 0:
	b = 16
	n = n.replace('0x',"")
elif n[0] == "0":
	b = 8
else:
	b = 10
n = n[::-1]

mul = 1
for i in n:
	if i.isdigit():
		num = int(i)
	else:
		num = alpha_low.index(i) + 10
	result += num * mul
	mul *= b
print(result)
