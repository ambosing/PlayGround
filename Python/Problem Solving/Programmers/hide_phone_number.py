def solution(phone_number):
    len_num = len(phone_number)
    answer = [phone_number[i] if i >= len_num - 4 else '*' for i in range(len_num)]
    answer = ''.join(answer)
    return answer
