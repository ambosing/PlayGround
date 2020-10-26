n = int(input())
adder = 1
res = 2
for i in range(n):
    res += adder
    adder *= 2

print(res ** 2)
