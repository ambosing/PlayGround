t = int(input())


def solution():
    min_year, min_mon, min_day = 2011, 2011, 2011
    max_year, max_mon, max_day = -1, -1, -1
    min_name, max_name = str(), str()
    for i in range(t):
        lst = input().split()
        name = lst.pop(0)
        day, mon, year = map(int,lst)
        if min_year > year:
            min_year = year
            min_name = name
            min_mon = mon
            min_day = day
        elif min_year == year:
            if min_mon > mon:
                min_mon = mon
                min_name = name
                min_day = day
            elif min_mon == mon:
                if min_day > day:
                    min_day = day
                    min_name = min
        if max_year < year:
            max_year = year
            max_name = name
            max_mon = mon
            max_day = day
        elif max_year == year:
            if max_mon < mon:
                max_mon = mon
                max_name = name
                max_day = day
            elif max_day == mon:
                if max_day == day:
                    max_day = day
                    max_name = name
    print(max_name)
    print(min_name)


solution()
