from sys import stdin

t = int(input())

for i in range(t):
    j, chars = stdin.readline().split()
    for char in chars:
        for k in range(int(j)):
            print(char, end="")
    print()