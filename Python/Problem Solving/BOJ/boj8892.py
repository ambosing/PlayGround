import sys


def same(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            s = a[i] + a[j]
            if s == s[::-1]:
                sys.stdout.write(s + "\n")
                return
            s = a[j] + a[i]
            if s == s[::-1]:
                sys.stdout.write(s + "\n")
                return
    sys.stdout.write("0\n")


for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        lst.append(input())
    same(lst)

