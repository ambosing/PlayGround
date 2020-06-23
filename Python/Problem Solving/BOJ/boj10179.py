t = int(input())

for i in range(t):
    price = float(input())
    price = round(price * 0.8, 2)
    print("$%.02f" % price)
