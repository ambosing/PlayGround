t = int(input())

for i in range(t):
    s = input()
    if s.count("+") > 0:
        a, b = map(int, s.split("+"))
        print(a + b)
    else:
        print("skipped")
