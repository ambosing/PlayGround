mod_lst = []

for i in range(10):
    mod = int(input()) % 42
    chk = 1
    for item in mod_lst:
        if item == mod:
            chk = 0
    if chk == 1:
        mod_lst.append(mod)

print(len(mod_lst))
