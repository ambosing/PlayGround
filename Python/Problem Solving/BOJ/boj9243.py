chk = 1

n = int(input()) % 2
s = input()
s2 = input()

for i in range(len(s)):
    if n == 1:
        if s[i] == s2[i]:
            chk = 0
    elif n == 0:
        if s[i] != s2[i]:
            chk = 0

if chk == 1:
    print("Deletion succeeded")
else:
    print("Deletion failed")
