import sys


class Queue:
    def __init__(self):
        self.f = 0
        self.b = 0
        self.queue = []

    def push(self, item):
        self.b += 1
        self.queue.append(item)

    def front(self):
        if self.empty():
            return -1
        return self.queue[self.f]

    def back(self):
        if self.empty():
            return -1
        return self.queue[self.b - 1]

    def size(self):
        if self.empty():
            return 0
        return self.b - self.f

    def empty(self):
        if self.f == self.b:
            return 1
        return 0

    def pop(self):
        if self.empty():
            return -1
        self.f += 1
        return self.queue[self.f - 1]


n = int(input())

queue = Queue()
for i in range(n):
    command = sys.stdin.readline().split()
    len_command = len(command)
    if len_command == 2:
        queue.push(command[1])
        continue
    if command[0] == "front":
        p = queue.front()
    elif command[0] == "back":
        p = queue.back()
    elif command[0] == "size":
        p = queue.size()
    elif command[0] == "empty":
        p = queue.empty()
    elif command[0] == "pop":
        p = queue.pop()
    sys.stdout.write(str(p) + "\n")
