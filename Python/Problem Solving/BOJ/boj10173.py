while True:
    s = input()
    if s.count("EOI") > 0:
        break
    s = s.lower()
    if s.count("nemo") > 0:
        print("Found")
    else:
        print("Missing")
