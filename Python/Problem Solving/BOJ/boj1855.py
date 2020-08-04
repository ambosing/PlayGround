import sys


def make_cipher(cipher_str, r, c):
    result = [[0 for _ in range(col)] for _ in range(row)]
    idx = 0

    for i in range(r):
        for j in range(c):
            if i % 2 == 1:
                j = c - j - 1
            result[i][j] = cipher_str[idx]
            idx += 1
    return result


def solution(cipher_str, r, c):
    cipher = make_cipher(cipher_str, row, col)
    decode_res = str()
    for i in range(c):
        for j in range(r):
            decode_res += cipher[j][i]
    return decode_res


col = int(input())
s = input()
row = len(s) // col
print(solution(s, row, col))
