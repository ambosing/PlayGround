ohm_color = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
ohm_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 0

for i in range(3):
    s = input()
    if i == 2:
        idx = ohm_color.index(s)
        limit = ohm_val[idx]
        for j in range(limit):
            result *= 10
    else:
        idx = ohm_color.index(s)
        result *= 10
        result += ohm_val[idx]
print(result)
