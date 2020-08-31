import sys


def rotate_left(letter):
    num = find_square_number(len(letter))
    lst = make_square(letter, num)
    res = [[0] * num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            res[j][i] = lst[i][num - j - 1]
    print_all(res, num)


def find_square_number(num):
    for i in range(num):
        if i * i == num:
            return i
    return num


def make_square(letter, num):
    lst = [[0] * num for _ in range(num)]
    idx = 0
    for i in range(num):
        for j in range(num):
            lst[i][j] = letter[idx]
            idx += 1
    return lst


def print_all(letter, num):
    for i in range(num):
        for j in range(num):
            sys.stdout.write(str(letter[i][j]))
    sys.stdout.write("\n")


for _ in range(int(input())):
    s = input()
    rotate_left(s)
