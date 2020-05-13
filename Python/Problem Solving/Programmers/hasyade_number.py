def solution(x):
    answer = True
    num = 0
    temp = x
    while temp > 0:
        num += temp % 10
        temp //= 10
    if x % num != 0:
        answer = False
    return answer
