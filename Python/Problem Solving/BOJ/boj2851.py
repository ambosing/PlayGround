def check_mario(chk):
    for i, c in enumerate(chk):
        if c == 1:
            for j in range(i + 1):
                if chk[j] == 0:
                    return False
    return True


def dfs(n, hap, chk):
    global num
    if n == 10:
        c = abs(100 - hap)
        d = abs(100 - num)
        if not check_mario(chk) or any(chk) == 0:
            return
        elif d == c:
            if hap > num:
                num = hap
        elif c < d:
            num = hap
        print(chk)
    else:
        chk[n] = 1
        dfs(n + 1, hap + lst[n], chk)
        chk[n] = 0
        dfs(n + 1, hap, chk)


check = [0] * 10
num = 0
lst = [int(input()) for _ in range(10)]
dfs(0, 0, check)
print(num)
