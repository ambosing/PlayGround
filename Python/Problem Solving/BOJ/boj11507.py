cards = input()
dic = {}
flag = False
card_dic = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
for idx in range(0, len(cards), 3):
    card = cards[idx:idx + 3]
    if card in dic:
        flag = True
        break
    else:
        dic[card] = 1
else:
    for key in dic.keys():
        card_dic[key[0]] -= 1
    for i, val in enumerate(card_dic.values(), start=1):
        if i != 4:
            print(val, end=" ")
        else:
            print(val)
if flag:
    print("GRESKA")