s = input()
lst = list()

for c in s:
    if c.isdigit():
        lst.append(c)
s = ''.join(lst)
num = int(s)
cnt = 0

for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)
