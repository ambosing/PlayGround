a, b, c = list(map(int, input().split()))

same = 1
money = 0
if a == b == c:
    same = 3
    money = a

elif a == b or b == c:
    same = 2
    money = b
elif a == c:
    same = 2
    money = c

elif a != b and b != c and a != c:
    if a > b > c or a > c > b:
        money = a
    if b > a > c or b > c > a:
        money = b
    if c > a > b or c > b > a:
        money = c

if same == 3:
    money = 10000 + money * 1000
elif same == 2:
    money = 1000 + money * 100
else:
    money = 100 * money
print(money)