d, m = map(int, input().split())

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = 2 + d
for i in range(m - 1):
    result += month[i]
print(days[result % 7])
