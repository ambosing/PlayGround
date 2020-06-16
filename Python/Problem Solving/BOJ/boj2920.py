asc = [i + 1 for i in range(8)]
desc = [i for i in range(8, 0, -1)]

asc_chk = 1
desc_chk = 1
lst = list(map(int, input().split()))
for i in range(8):
    if asc[i] != lst[i]:
        asc_chk = 0
    if desc[i] != lst[i]:
        desc_chk = 0

if asc_chk == 1:
    print("ascending")
elif desc_chk == 1:
    print("descending")
else:
    print("mixed")