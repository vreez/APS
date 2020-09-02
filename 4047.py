import sys
sys.stdin = open("4047.txt")

T = int(input())
for tc in range(1, T + 1):
    cards = list(input())

    card_list = []
    my_card = ''
    for i in range(0, len(cards)):
        if i == 0 or i % 3 != 0:
            my_card += cards[i]
        elif i % 3 == 0:
            card_list.append(my_card)
            my_card = ''
            my_card += cards[i]
    card_list.append(my_card)

    S = 13
    D = 13
    H = 13
    C = 13

    if len(card_list) == len(set(card_list)):
        for n in range(len(card_list)):
            if card_list[n][0] == 'S':
                S -= 1
            elif card_list[n][0] == 'D':
                D -= 1
            elif card_list[n][0] == 'H':
                H -= 1
            elif card_list[n][0] == 'C':
                C -= 1

        new_list = [S, D, H, C]

        print("#{}".format(tc), *new_list)
    else:
        print("#{} {}".format(tc, 'ERROR'))