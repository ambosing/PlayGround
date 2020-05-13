def solution(dartResult):
    answer = []
    lst = list(dartResult)
    temp = 0
    idx = -1
    for i in range(len(lst)):
        if lst[i] == "D" or lst[i] == "S" or lst[i] == "T":
            if lst[i] == "D":
                temp **= 2
            elif lst[i] == "T":
                temp **= 3
        elif lst[i] == "*" or lst[i] == "#":
            if lst[i] == "*":
                temp *= 2
                answer[idx] *= 2
            else:
                temp *= -1
        else:
            try:
                if lst[i] == '0' and lst[i - 1] == '1':
                    continue
            except:
                pass
            answer.append(temp)
            idx += 1
            temp = 0
            temp += int(lst[i])
            try:
                if lst[i] == '1' and lst[i + 1] == '0':
                    temp *= 10
            except:
                pass
    answer.append(temp)
    return sum(answer)