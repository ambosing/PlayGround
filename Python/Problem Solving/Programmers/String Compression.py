def solution(s):
    len_s = len(s)
    min_len = 1001
    i = 1
    while i <= len_s:
        end = i
        start = 0
        temp_len = len_s
        temp = 1
        pre = s[start:end]
        while end < len_s:
            start += i
            end += i
            cur = s[start:end]
            if cur == pre:
                temp_len -= i
                temp += 1
            if end == len_s or cur != pre:
                if temp != 1:
                    temp_len += len(str(temp))
                temp = 1
            pre = cur
        if min_len > temp_len:
            min_len = temp_len
        i += 1
    return min_len
