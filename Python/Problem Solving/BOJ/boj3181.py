s = input().split()
lst = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
result = ""

for i, v in enumerate(s):
    if i != 0 and v in lst:
        continue
    result += v[0].upper()
print(result)
