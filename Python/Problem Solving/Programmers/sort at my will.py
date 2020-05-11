def solution(strings, n):
    answer = []
    len_strings = len(strings)
    for i in range(len_strings):
        strings[i] = strings[i][n] + strings[i]
    
    strings.sort()
    print(strings)
    
    for j in range(len_strings):
        answer.append(strings[j][1:])

    return answer
