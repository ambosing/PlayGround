s = input()
stack = []

for c in s:
    if stack and c == ')' and stack[-1] == '(':
        stack.pop()
    else:
        stack.append(c)
print(len(stack))
