import sys

t = int(input())

for i in range(t):
    carPrice = int(sys.stdin.readline().rstrip())
    optionNum = int(sys.stdin.readline().rstrip())
    totalPrice = 0
    for j in range(optionNum):
        num, optionPrice = map(int, sys.stdin.readline().rstrip().split())
        totalPrice += num * optionPrice
    totalPrice += carPrice
    sys.stdout.write(str(totalPrice) + "\n")
