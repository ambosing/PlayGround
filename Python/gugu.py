#!usr/bin/python3

for i in range(2,9):
    for j in range(1,9):
        print("%d x %d = %d" %(i, j, i*j))

k = 2
l = 1
while(k <10):
    while(l <10):
        print("%d x %d = %d" %(k, l, k*l))
        l = l + 1

    l = 1
    k = k + 1
