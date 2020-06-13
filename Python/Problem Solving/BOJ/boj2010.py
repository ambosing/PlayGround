import sys

n = int(input())
totalPlugNum = 0

for i in range(n):
    plugNum = int(sys.stdin.readline())
    if totalPlugNum == 0:
        totalPlugNum = plugNum
        continue
    totalPlugNum += plugNum - 1

print(totalPlugNum)
