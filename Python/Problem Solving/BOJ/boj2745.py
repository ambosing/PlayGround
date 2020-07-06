import string

n, b = input().split()
alpha_up = list(string.ascii_uppercase)
len_n = len(n)
b = int(b)
mul = 1
result = 0
for i in range(len_n - 1, -1, -1):
	if n[i].isdigit():
		num = int(n[i])
	else:
		num = alpha_up.index(n[i]) + 10
	result += num * mul
	mul *= b
print(result)
