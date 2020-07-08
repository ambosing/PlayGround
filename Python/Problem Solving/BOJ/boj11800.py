lst = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]

for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        if a == 1:
            s = "Habb Yakk"
        elif a == 2:
            s = "Dobara"
        elif a == 3:
            s = "Dousa"
        elif a == 4:
            s = "Dorgy"
        elif a == 5:
            s = "Dabash"
        elif a == 6:
            s = "Dosh"
        print("Case %d: %s" % (i + 1, s))
        continue
    if (a == 5 and b == 6) or (a == 6 and b == 5):
        print("Case %d: Sheesh Beesh" % (i + 1))
    else:
        print("Case %d: %s %s" % (i + 1, lst[max(a, b) - 1], lst[min(a, b) - 1]))
