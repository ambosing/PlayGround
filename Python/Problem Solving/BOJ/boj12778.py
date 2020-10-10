from string import ascii_uppercase

alpha_up = ascii_uppercase


def c_type(problem):
    res = list()
    for c in problem:
        res.append(str(alpha_up.index(c) + 1))
    return res


def n_type(problem):
    res = list()
    for i in problem:
        res.append(alpha_up[int(i) - 1])
    return res


for _ in range(int(input())):
    m, t = input().split()
    s = input().split()
    if t == "C":
        result = c_type(s)
    elif t == "N":
        result = n_type(s)
    print(" ".join(result))
