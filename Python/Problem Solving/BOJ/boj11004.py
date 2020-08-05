import sys

lst = []
for _ in range(int(input())):
    lst.append(int(sys.stdin.readline()))

lst.sort(reverse=True)

for i in lst:
    sys.stdout.write(str(i) + "\n")
