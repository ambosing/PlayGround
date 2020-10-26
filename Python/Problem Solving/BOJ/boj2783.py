a, b = map(int, input().split())
min_val = a / b
min_gram = b
min_cost = a
for _ in range(int(input())):
    a, b = map(int, input().split())
    if min_val > a / b:
        min_gram = b
        min_cost = a
        min_val = a / b

print("%.2f" % (round((1000 / min_gram) * min_cost, 2)))
