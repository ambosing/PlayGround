magic = [1, 2, 3, 3, 4, 10]
enemy = [1, 2, 2, 2, 3, 5, 10]

for i in range(int(input())):
    m_score = 0
    e_score = 0
    m = list(map(int, input().split()))
    e = list(map(int, input().split()))
    for idx, value in enumerate(magic):
        m_score += value * m[idx]
    for idx, value in enumerate(enemy):
        e_score += value * e[idx]
    if m_score > e_score:
        print("Battle %d: Good triumphs over Evil" % (i + 1))
    elif m_score < e_score:
        print("Battle %d: Evil eradicates all trace of Good" % (i + 1))
    else:
        print("Battle %d: No victor on this battle field" % (i + 1))
