def is_empty(st):
    if st:
        return 0
    return 1


def is_mul_div(st, res, op):
    if op == '*' or op == '/':
        while not is_empty(st) and (st[-1] == '*' or st[-1] == '/'):
            res.append(st.pop())
        st.append(op)


def is_plus_minus(st, res, op):
    if op == '+' or op == '-':
        if is_empty(st):
            st.append(op)
        else:
            while not is_empty(st) and st[-1] != '(':
                res.append(st.pop())
            st.append(op)


def is_bracket(st, res, op):
    if c == '(':
        stack.append(c)
    elif c == ')':
        ch = op
        while ch != '(':
            ch = st.pop()
            if ch == '(':
                break
            res.append(ch)


s = input()
stack = []
result = []
for c in s:
    if c.isdigit():
        result.append(c)
    else:
        is_mul_div(stack, result, c)
        is_plus_minus(stack, result, c)
        is_bracket(stack, result, c)
while stack:
    result.append(stack.pop())
print(''.join(result))
