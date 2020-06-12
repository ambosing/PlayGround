import sys

schoolNum = int(input())
result = 0
for i in range(schoolNum):
    studentNum, apple = map(int, sys.stdin.readline().rstrip().split())
    div = apple // studentNum
    result += apple - div * studentNum
print(result)
