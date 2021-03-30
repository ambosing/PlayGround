s = list(map(int, input()))
a = sum(s[:len(s) // 2])
b = sum(s[len(s) // 2:])
if a == b:
    print("LUCKY")
else:
    print("READY")
