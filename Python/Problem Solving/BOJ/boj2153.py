import string


def is_prime(x):
    i = 2
    while i <= x // i:
        if x % i == 0:
            return False
        i += 1
    return True


alpha = list(string.ascii_lowercase + string.ascii_uppercase)
s = input()
num = 0
for c in s:
    idx = alpha.index(c)
    num += idx + 1
if is_prime(num):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
