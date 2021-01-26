s = input()
num = ""
for c in s:
    if c.isnumeric():
        num += c
num = int(num)
cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)
