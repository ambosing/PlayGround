def next_permutation(x):
    len_x = len(x) - 1
    i = len_x
    while i > 0 and ord(x[i - 1]) >= ord(x[i]):
        i -= 1
    if i == 0:
        return False
    j = len_x
    while ord(x[i - 1]) >= ord(x[j]):
        j -= 1
    x[i - 1], x[j] = x[j], x[i - 1]
    j = len_x
    while i < j:
        x[i], x[j] = x[j], x[i]
        i += 1
        j -= 1
    return True


for _ in range(int(input())):
    s = list(input())
    s_ = s.copy()
    if next_permutation(s):
        print(''.join(s))
    else:
        print(''.join(s_))
