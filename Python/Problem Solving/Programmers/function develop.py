import math

def solution(progresses, speeds):
    answer = []
    day = 0
    progress_len = len(progresses)
    for i in range(progress_len):
        if progresses[i] == -1:
            continue
        temp = 0
        day = int(math.ceil((100 - progresses[i]) / speeds[i]))
        temp += 1
        for j in range(i + 1, progress_len):
            if progresses[j] + speeds[j] * day >= 100:
                temp += 1
                progresses[j] = -1
            else:
                break
        answer.append(temp)
    return answer
