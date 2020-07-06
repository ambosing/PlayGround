while True:
	try:
		a, b = map(int, input().split())
		print("%0.2f" % (a / b))
	except EOFError:
		break