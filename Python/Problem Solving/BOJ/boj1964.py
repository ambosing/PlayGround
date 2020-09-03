n = int(input())
res = 0
adder = 2
plus = 5
for i in range(n):
    res += plus
    plus += adder
    if adder < 3:
        adder += 1
print(res % 45678)
