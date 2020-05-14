from string import ascii_uppercase


def find_idx(alp, now, pre, check, idx):
    pre_idx = 0
    now_idx = 0
    for i in range(26):
        if alp[i] == pre:
            pre_idx = i
            break
    for i in range(26):
        if alp[i] == now:
            now_idx = i
            break
    if pre_idx == now_idx or check[idx] == 1:
        check[idx] = 1
        return 100
    for i in range(1, 26):
        if (pre_idx + i) % 26 == now_idx:
            return i
        if (pre_idx - i) % 26 == now_idx:
            return i
    return 0


def all_finish(check):
    for i in range(len(check)):
        if check[i] == 0:
            return True
    return False


def solution(name):
    answer = 0
    alpha = ascii_uppercase
    len_name = len(name)
    problem = ["A"] * len_name
    check = [0] * len_name
    idx = 0
    if name[0] != "A":
        answer += find_idx(alpha, name[0], problem[0], check, idx)
    check[idx] = 1
    while all_finish(check):
        for s in range(1, len_name):
            left_idx = (idx - s) % len_name
            right_idx = (idx + s) % len_name
            left = find_idx(alpha, name[left_idx], problem[idx], check, left_idx)
            right = find_idx(alpha, name[right_idx], problem[idx], check, right_idx)
            if check[left_idx] == 0 and left < right:
                answer += left + s
                idx = left_idx
                check[idx] = 1
                break
            if check[right_idx] == 0 and right <= left:
                answer += right + s
                idx = right_idx
                check[idx] = 1
                break
    return answer
