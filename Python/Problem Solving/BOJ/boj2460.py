max_people = 0
people = 0

for i in range(10):
    off_people, on_people = map(int, input().split())
    people = on_people if people == 0 else people - off_people + on_people
    max_people = people if max_people < people else max_people

print(max_people)
