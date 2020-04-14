def solution(board, moves):
    answer = 0
    temp = []
    for move in moves:
        idx = move - 1
        leng = len(board[idx])
        for i in range(leng):
            val = board[i][idx]
            if val != 0:
                temp.append(val)
                temp_len = len(temp)
                if  temp_len > 1 and temp[temp_len - 2] == val:
                    temp.pop()
                    temp.pop()
                    answer += 2
                board[i][idx] = 0
                pre = val
                break
    return answer
