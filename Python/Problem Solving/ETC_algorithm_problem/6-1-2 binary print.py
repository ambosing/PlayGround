def make_binary(a):
    if a == 0:
        return
    else:
        make_binary(a // 2)
        print(a % 2, end="")


n = int(input())
make_binary(n)
