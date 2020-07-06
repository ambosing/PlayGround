for _ in range(int(input())):
	n = input().lower()
	rev_n = n[::-1]
	if n == rev_n:
		print("Yes")
	else:
		print("No")
