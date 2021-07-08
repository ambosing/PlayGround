def rotate_left_90(key, k1, k2):
    result = [[0] * k1 for _ in range(k2)]
    for i in range(k2):
        for j in range(k1):
            result[k1 - i - 1][j] = key[j][i]
    return result, k2, k1


def check(big_lock, lock_len, big_lock_len):
    for i in range(lock_len, big_lock_len - lock_len):
        for j in range(lock_len, big_lock_len - lock_len):
            if big_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    big_lock = []
    lock_len = len(lock)
    for i in range(lock_len * 3):
        if lock_len <= i < lock_len * 2:
            add_list = [0] * lock_len + lock[i - lock_len] + [0] * lock_len
            big_lock.append(add_list)
        else:
            big_lock.append([0] * lock_len * 3)
    big_lock_len = lock_len * 3
    k1 = len(key)
    k2 = len(key[0])
    for i in range(lock_len * 2):
        for j in range(lock_len * 2):
            for k in range(4):
                key, k1, k2 = rotate_left_90(key, k1, k2)
                for a in range(k1):
                    for b in range(k2):
                        big_lock[i + a][j + b] += key[a][b]
                if check(big_lock, lock_len, big_lock_len):
                    return True
                for a in range(k1):
                    for b in range(k2):
                        big_lock[i + a][j + b] -= key[a][b]
    return answer
