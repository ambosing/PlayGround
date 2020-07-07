def swap(lst, ii, jj):
    temp = lst[ii]
    lst[ii] = lst[jj]
    lst[jj] = temp


lst_ = input().split()
n = 5
while True:
    for i in range(n - 1):
        if lst_[i] > lst_[i + 1]:
            swap(lst_, i, i + 1)
            print(' '.join(lst_))
    chk = True
    for i in range(n):
        if lst_[i] != str(i + 1):
            chk = False
    if chk:
        break
