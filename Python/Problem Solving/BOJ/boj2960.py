def solution():
    n, k = map(int, input().split())
    prime_lst = [True] * (n + 1)
    cnt = 0

    for i in range(2, n + 1):
        if not prime_lst[i]:
            continue
        cnt += 1
        if cnt == k:
            print(i)
            return
        for j in range(i + i, n + 1, i):
            if not prime_lst[j]:
                continue
            prime_lst[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                return


solution()
