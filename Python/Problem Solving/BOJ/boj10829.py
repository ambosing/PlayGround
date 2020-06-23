num = int(input())
lst = []
while num > 0:
    lst.append(str(num % 2))
    num //= 2
s = ''.join(lst).rstrip("0")
s = s[::-1]
print(s)
