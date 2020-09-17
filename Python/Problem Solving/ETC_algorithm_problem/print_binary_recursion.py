import sys


def binary_print(num):
    if num == 0:
        return
    binary_print(num // 2)
    sys.stdout.write(str(num % 2))


n = int(input())
binary_print(n)