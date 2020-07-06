import string

n, b = map(int, input().split())
alpha_up = list(string.ascii_uppercase)
lst = []

while n > 0:
	num = n % b
	if num >= 10:
		num = alpha_up[num - 10]
	lst.append(str(num))
	n //= b
lst = lst[::-1]
print(''.join(lst))
