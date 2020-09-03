while True:
    lst = list(input().split())
    if lst[0][0] == '*':
        break
    for i in range(len(lst) - 1):
        if lst[i][0].lower() != lst[i + 1][0].lower():
            print('N')
            break
    else:
        print('Y')
