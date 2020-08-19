def make_prime_list(num):
    prime_list = [True] * (num + 1)
    for i in range(2, num + 1):
        if not prime_list[i]:
            continue
        for j in range(i + i, num + 1, i):
            prime_list[j] = False
    return prime_list


def prime_count(prime_list, start):
    end = start * 2 + 1
    count = 0
    for i in range(start + 1, end):
        if prime_list[i]:
            count += 1
    return count


def solution():
    lst = []
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            lst.append(n)
    prime_list = make_prime_list(max(lst) * 2)
    for item in lst:
        print(prime_count(prime_list, item))


solution()
