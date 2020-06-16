div = int(input())

while True:
    num = int(input())
    if num == 0:
        break
    if num % div == 0:
        print("%d is a multiple of %d." % (num, div))
    else:
        print("%d is NOT a multiple of %d." % (num, div))