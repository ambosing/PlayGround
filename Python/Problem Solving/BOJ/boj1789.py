s = int(input())

num = 1
while num * (num + 1) / 2 <= s:
    num += 1
print(num - 1)
