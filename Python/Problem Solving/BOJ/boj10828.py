import sys


class Stack:
    def __init__(self):
        self.t = 0
        self.stack = []

    def push(self, item):
        self.t += 1
        self.stack.append(item)

    def top(self):
        if self.empty():
            return -1
        return self.stack[self.t - 1]

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.t == 0:
            return 1
        return 0

    def pop(self):
        if self.empty():
            return -1
        self.t -= 1
        return self.stack.pop()


n = int(input())

stack = Stack()
for i in range(n):
    command = sys.stdin.readline().split()
    len_command = len(command)
    if len_command == 2:
        stack.push(command[1])
        continue
    if command[0] == "top":
        p = stack.top()
    elif command[0] == "size":
        p = stack.size()
    elif command[0] == "empty":
        p = stack.empty()
    elif command[0] == "pop":
        p = stack.pop()
    sys.stdout.write(str(p) + "\n")
