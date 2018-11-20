#!usr/bin/python3


a = [88, 98, 96, 77, 63]
b = [86, 77, 66, 86, 93]
c = [74, 83, 95, 86, 97]

sum1 = 0

for item in a:
    sum1 = sum1 + item
avg = sum1 / 5
print("sum = %d avg = %d" %(sum1, avg))

sum1 = 0
for item in b:
    sum1 = sum1 + item
avg = sum1 / 5
print("sum = %d avg = %d" %(sum1, avg))

sum1 = 0
for item in c:
    sum1 = sum1 + item
avg = sum1 / 5
print("sum = %d avg = %d" %(sum1, avg))

sum1 = 0
d = [a,b,c]
for item in d:
    for i in item:
        sum1 = sum1 + i

    avg = sum1 / 5
    print("sum = %d avg = %d" %(sum1, avg))
    sum1 = 0

