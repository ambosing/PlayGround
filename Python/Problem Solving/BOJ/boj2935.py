def operate_plus(len_aa, len_bb):
    if len_aa > len_bb:
        print("1", end="")
        for i in range(len_aa - 1):
            if len_aa - len_bb - 1 == i:
                print("1", end="")
            else:
                print("0", end="")
        print()

    elif len_bb > len_aa:
        print("1", end="")
        for i in range(len_bb - 1):
            if len_bb - len_aa - 1 == i:
                print("1", end="")
            else:
                print("0", end="")

    else:
        print("2", end="")
        for i in range(len_bb - 1):
            print("0", end="")


def operate_multiply(aa, bb, len_aa, len_bb):
    if aa[0] == '0' or bb[0] == '0':
        print("0")
    print("1", end="")
    for i in range(len_aa + len_bb - 2):
        print("0", end="")


def processing(a, b, len_aa, len_bb, al_operator):
    if al_operator == '*':
        operate_multiply(a, b, len_aa, len_bb)

    elif al_operator == "+":
        operate_plus(len_aa, len_bb)


a = input()
operator = input()
b = input()
len_a = len(a)
len_b = len(b)

if a[0] == '0' and b[0] == '0':
    print("0")
else:
    processing(a, b, len_a, len_b, operator)
