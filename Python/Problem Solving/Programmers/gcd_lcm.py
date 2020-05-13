def solution(n, m):
    a, b = n, m
    while b != 0:
        temp = a
        a = b
        b = temp % b
    answer = [a, (m * n) // a]
    return answer
