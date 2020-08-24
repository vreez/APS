import sys
sys.stdin = open('GNS_test_input.txt')

N = int(input())
for n in range(1, N+1):
    t = input()
    T = list(input().split())

    number = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}


    my_list = []
    for i in T:
        my_list.append(number[i])

    for j in range(len(my_list) - 1, 0, -1):
        for k in range(0, j):
            if my_list[k] > my_list[k + 1]:
                my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]

    new_number = {value: key for key, value in
                  number.items()}

    new_list = []
    for m in my_list:
        new_list.append(new_number[m])


    print('#{}'.format(n))
    print(' '.join(new_list))

