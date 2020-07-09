from functools import cmp_to_key


def digit_sum(l):
    hap = 0
    for i in l:
        if i.isdigit():
            hap += int(i)
    return hap


def cmp(a, b):
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        return len_a - len_b
    else:
        hap_a = digit_sum(a)
        hap_b = digit_sum(b)
        if hap_a != hap_b:
            return hap_a - hap_b
        else:
            for i, v in enumerate(a):
                if a[i] != b[i]:
                    return ord(a[i]) - ord(b[i])
    return 0


lst = []
for _ in range(int(input())):
    lst.append(input())
lst = sorted(lst, key=cmp_to_key(cmp))
print('\n'.join(lst))
