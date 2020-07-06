n = int(input())

if n == 1:
	print(1)
else:
	chk = True
	while n > 2:
		if n % 2 != 0:
			print(0)
			chk = False
			break
		n //= 2
	if chk:
		print(1)