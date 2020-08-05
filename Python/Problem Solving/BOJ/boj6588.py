import sys


def make_prime_list(n):
    prime_check = [True] * (n + 1)
    prime_lst = []

    for i in range(2, n + 1):
        if not prime_check[i]:
            continue
        if i % 2 == 1:
            prime_lst.append(i)
        for j in range(i + i, n + 1, i):
            if not prime_check[j]:
                continue
            prime_check[j] = False
    return prime_lst


def find_max_index(prime_lst, target):
    for i, v in enumerate(prime_lst):
        if v >= target:
            return i - 1
    return i


def print_arithmetic_expression(target, min_val, max_val):
    sys.stdout.write(str(target) + " = " +
                     str(min_val) +
                     " + " + str(max_val) + "\n")


def prime_sum(prime_lst, target):
    max_idx = find_max_index(prime_lst, target)
    min_idx = 0

    while min_idx <= max_idx:
        num = prime_lst[min_idx] + prime_lst[max_idx]
        if target == num:
            print_arithmetic_expression(target, prime_lst[min_idx], prime_lst[max_idx])
            return
        elif target < num:
            max_idx -= 1
        else:
            min_idx += 1
    sys.stdout.write("Goldbach's conjecture is wrong.\n")


def solution():
    lst = list()
    while True:
        n = int(input())
        if n == 0:
            break
        lst.append(n)
    prime_lst = make_prime_list(max(lst))

    for i in lst:
        prime_sum(prime_lst, i)


solution()
