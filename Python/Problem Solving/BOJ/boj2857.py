lst = []
for i in range(5):
    s = input()
    if s.count("FBI") > 0:
        lst.append(i + 1)

if len(lst) == 0:
    print("HE GOT AWAY!")
else:
    for i in lst:
        print(i, end=" ")
