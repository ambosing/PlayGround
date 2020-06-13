numCar = int(input())
lst = map(int, input().split())
cnt = 0

for i in lst:
    if i == numCar:
        cnt += 1

print(cnt)