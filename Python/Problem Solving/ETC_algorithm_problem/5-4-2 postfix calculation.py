s = input()
nums = []
operator = ['+', '-', '*', '/']
for c in s:
    if c in operator:
        b = int(nums.pop())
        a = int(nums.pop())
        if c == operator[0]:
            nums.append(a + b)
        elif c == operator[1]:
            nums.append(a - b)
        elif c == operator[2]:
            nums.append(a * b)
        elif c == operator[3]:
            nums.append(a // b)
    else:
        nums.append(c)
print(nums[0])
