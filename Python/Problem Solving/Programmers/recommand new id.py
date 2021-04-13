def step1(id):
    new_id = []
    for i, c in enumerate(id):
        if not(c.isalpha() or c == '.' or c == '-' or c == '_' or c.isdigit()):
            continue
        if c.isalpha():
            new_id.append(c.lower())
        elif c == '.' and (i == 0 or i == len(id) - 1):
            continue
        elif i != 0 and id[i - 1] == '.':
            continue
        else:
            new_id.append(c)
    if not new_id:
        return "a"
    return "".join(new_id)


def step2(id):
    idx = len(id)
    while idx >= 0 and id[idx] == ".":
        id.pop()
        idx -= 1
    if len(id) > 15:
        new_id = list(id[:15])
        if new_id[14] == '.':
            new_id.pop()
    else:
        new_id = list(id)
    if len(new_id) <= 2:
        for i in range(3):
            new_id.append(new_id[len(new_id) - 1])
            if len(new_id) >= 3:
                break
    return "".join(new_id)


def solution(new_id):
    answer = step1(new_id)
    answer = step2(answer)
    return answer