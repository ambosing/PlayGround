maxPeople = 0
num = 0

for i in range(4):
    offPeople, OnPeople = map(int, input().split())
    num += OnPeople - offPeople
    maxPeople = num if maxPeople < num else maxPeople
print(maxPeople)
