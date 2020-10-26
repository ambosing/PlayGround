a, b = map(int, input().split())

col1 = (a - 1) // 4
row1 = (col1 + 1) * 4 - a
col2 = (b - 1) // 4
row2 = (col2 + 1) * 4 - b

print(abs(col2 - col1) + abs(row2 - row1))
