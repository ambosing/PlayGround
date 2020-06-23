mon = int(input())
day = int(input())

if mon > 2:
    print("After")
if mon == 2:
    if day == 18:
        print("Special")
    if day > 18:
        print("After")
    if day < 18:
        print("Before")
if mon < 2:
    print("Before")
