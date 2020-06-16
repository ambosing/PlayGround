t = int(input())
seat = [0] * 100
people = list(map(int, input().split()))
deny_cnt = 0
for item in people:
    if seat[item - 1] == 1:
        deny_cnt += 1
    else:
        seat[item - 1] = 1

print(deny_cnt)
