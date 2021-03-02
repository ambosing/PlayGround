s = input()
operator = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
stack = []
for c in s:
    if c in operator:
        while stack and stack[-1] != '(' and operator[stack[-1]] >= operator[c]:
            print(stack.pop(), end="")
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            print(stack.pop(), end="")
        stack.pop()
    else:
        print(c, end="")
while stack:
    print(stack.pop(), end="")
