s = input()
happy_cnt = s.count(":-)")
sad_cnt = s.count(":-(")

if happy_cnt == 0 and sad_cnt == 0:
    print("none")
elif happy_cnt > sad_cnt:
    print("happy")
elif sad_cnt > happy_cnt:
    print("sad")
elif sad_cnt == happy_cnt:
    print("unsure")
