def step1(origin):
    new = []
    for i, c in enumerate(origin):
        if c.isalpha() or c.isdigit() or c == '.' or c == '-' or c == '_':
            if c == '.' and new and new[-1] == '.':
                continue
            new.append(c.lower())
    return new


def step2(origin):
    while origin and origin[0] == '.':
        origin.pop(0)
    while origin and origin[-1] == '.':
        origin.pop()
    if not origin:
        return "a"
    return origin


def step3(origin):
    origin = list(origin)
    if len(origin) > 15:
        new = origin[:15]
        while new[-1] == '.':
            new.pop()
    else:
        new = origin
    for i in range(3):
        if len(new) >= 3:
            break
        new.append(new[-1])
    return "".join(new)


def solution(new_id):
    answer = step1(new_id)
    answer = step2(answer)
    answer = step3(answer)
    return answer