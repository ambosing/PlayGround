import string
import sys

alpha = string.ascii_uppercase
alpha_hap = 0
for val in alpha:
    alpha_hap += ord(val)

t = int(input())

for i in range(t):
    s = sys.stdin.readline().rstrip()
    lst = []
    for item in s:
        chk = True
        for item2 in lst:
            if item2 == item:
                chk = False
        if chk:
            lst.append(item)
    temp = 0
    for item in lst:
        temp += ord(item)
    sys.stdout.write(str(alpha_hap - temp) + "\n")
