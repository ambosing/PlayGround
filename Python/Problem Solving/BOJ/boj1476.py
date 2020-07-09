e, s, m = map(int, input().split())
e_, s_, m_ = 1, 1, 1
i = 1
while True:
    if e == e_ and s == s_ and m == m_:
        break
    e_ += 1
    s_ += 1
    m_ += 1
    if e_ > 15:
        e_ = 1
    if s_ > 28:
        s_ = 1
    if m_ > 19:
        m_ = 1
    i += 1
print(i)
