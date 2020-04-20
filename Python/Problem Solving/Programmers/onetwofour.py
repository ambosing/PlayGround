def solution(n):
    answer = ''
    temp = 0
    n -= 1
    while n > -1:
        temp = n % 3
        if temp == 0:
            answer += '1'
        elif temp == 1:
            answer += '2'
        else:
            answer += '4'
        n = n // 3
        n -= 1
    answer = answer[::-1]
    return answer
