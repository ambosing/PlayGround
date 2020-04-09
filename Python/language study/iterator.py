a = [1, 2, 3]
print(dir(a))

it = [1, 2, 3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())

class Counter:
    def __init__(self, stop):
        self.current = -1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration

for i in Counter(3):
    print(i, end = ' ')
print()

class Counter2:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError


print(Counter2(3)[0], Counter2(3)[1], Counter2(3)[2])

for i in Counter2(3):
    print(i, end=' ')
print()

it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))
'''
import random
it = iter(lambda : random.randint(0, 5), 2)
print(next(it))
print(next(it))
print(next(it))
'''
class MultipleIterator:
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.multiple
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration

for i in MultipleIterator(20, 3):
    print(i, end=' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')
print()

class TimeIterator():
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop
        self.hour = start // 3600
        self.minute = (start % 3600) // 60
        self.sec = start % 60 - 1

    def over_sec(self):
        if self.sec >= 60:
            self.minute += self.sec // 60
            self.sec = self.sec % 60
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute = self.minute % 60
        if self.hour >= 24:
            self.hour = self.hour % 24
            self.minute = self.minute % 60
            self.sec = self.sec % 60

    def get_time(self):
        temp = str(self.hour).zfill(2)
        temp1 = str(self.minute).zfill(2)
        temp2 = str(self.sec).zfill(2)
        time = temp + ":" + temp1 + ":" + temp2
        return time

    def __getitem__(self, index):
        if index < (self.stop - self.start):
            temp = self.start + index + 1
            self.hour = temp // 3600
            self.minute = (temp % 3600) // 60
            self.sec = temp % 60
            self.over_sec()
            item = self.get_time()
            return item
        else:
            raise IndexError

    def __iter__(self):
        return self

    def __next__(self):
        self.sec += 1
        self.start += 1
        self.over_sec()
        if self.start < self.stop:
            time = self.get_time()
            return time
        else:
            raise StopIteration

start, stop, index = map(int, input().split())

for i in TimeIterator(start, stop):
    print(i)

print('\n', TimeIterator(start, stop)[index], sep='')