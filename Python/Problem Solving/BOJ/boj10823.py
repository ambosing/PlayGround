import sys

s = ''.join(sys.stdin.readlines())
lst = s.split("\n")
s = ''.join(lst)
lst = s.split(",")
result = 0
for i in lst:
    result += int(i)
print(result)

