def solution(number, k):
    answer = ""
    ans_len = len(number) - k
    for i, v in enumerate(number):
        rem = len(number) - i
        if answer:
            answer += v
        elif i < ans_len + len(answer):
            for ii, c in enumerate(answer):
                if int(c) < int(v):
                    answer[ii] = v
                else:
                    answer += v
                    break
        else:
            s = len(answer) - rem
            for ii in range(0, ans_len):
                if int(answer[ii]) < int(v):
                    answer[ii] = v
                else:
                    answer[ii] += v
    return answer


print(solution("1924", 2))
