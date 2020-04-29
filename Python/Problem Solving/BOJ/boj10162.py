t = int(input())

mm = 300
m = 60
s = 10

mm_res = t // mm
t %= mm
m_res = t // m
t %= m
s_res = t // s
t %= s

if t != 0:
    print(-1)
else:
    print(mm_res, m_res, s_res)
