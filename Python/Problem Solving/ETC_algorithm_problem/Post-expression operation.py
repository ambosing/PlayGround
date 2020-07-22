s = input()
stack = []
for item in s:
    if item.isdecimal():
        stack.append(item)
    else:
        b = int(stack.pop())
        a = int(stack.pop())
        if item == '+':
            val = a + b
        elif item == '-':
            val = a - b
        elif item == '*':
            val = a * b
        elif item == '/':
            val = a // b
        stack.append(val)
print(stack[0])

