cnt = 0
while True:
    lower_cnt = 0
    upper_cnt = 0
    digit_cnt = 0
    space_cnt = 0
    cnt += 1
    if cnt > 100:
        break
    try:
        s = input()
    except:
        break
    for c in s:
        if c.islower():
            lower_cnt += 1
        elif c.isupper():
            upper_cnt += 1
        elif c.isdigit():
            digit_cnt += 1
        else:
            space_cnt += 1
    print(lower_cnt, upper_cnt, digit_cnt, space_cnt)
