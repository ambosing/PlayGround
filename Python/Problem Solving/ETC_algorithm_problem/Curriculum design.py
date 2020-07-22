def is_unique(lsn, st):
    if st.count(lsn) > 0:
        return False
    return True


def is_necessary(lsn, nec):
    if nec.count(lsn) > 0:
        return True
    return False


nec_str = input()

for i in range(int(input())):
    s = ""
    lesson = input()
    for c in lesson:
        if is_necessary(c, nec_str) and is_unique(c, s):
            s += c
        if s == nec_str:
            print("#%d YES" % (i + 1))
            break
    else:
        print("#%d NO" % (i + 1))

