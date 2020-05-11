def solution(s):
    answer = ''
    len_s = len(s)
    if len_s % 2 == 0:
        answer += s[len_s // 2 - 1] + s[len_s // 2]
    else:
        answer += s[len_s // 2]
    return answer
