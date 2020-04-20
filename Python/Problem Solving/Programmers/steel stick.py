def solution(arrangement):
    answer = 0
    cnt_steel = 0
    len_arr = len(arrangement)
    i = 0
    while i < len_arr:
        if (i + 1 < len_arr and arrangement[i] == '(' and arrangement[i + 1] == ')'):
            answer += cnt_steel
            i += 2
            continue
        if (arrangement[i] == '('):
            cnt_steel += 1
        elif (arrangement[i] == ')'):
            answer += 1
            cnt_steel -= 1
        i += 1
    return answer
