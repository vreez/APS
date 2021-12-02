import sys; sys.stdin = open("23027.txt", "r")

letter = list(input())

if 'A' in letter:
    for i in range(len(letter)):
        if letter[i] == 'B' or letter[i] == 'C' or letter[i] == 'D' or letter[i] == 'F':
            letter[i] = 'A'
elif 'A' not in letter and 'B' in letter:
    for i in range(len(letter)):
        if letter[i] == 'C' or letter[i] == 'D' or letter[i] == 'F':
            letter[i] = 'B'
elif 'A' not in letter and 'B' not in letter and  'C' in letter:
    for i in range(len(letter)):
        if letter[i] == 'D' or letter[i] == 'F':
            letter[i] = 'C'
elif 'A' not in letter and 'B' not in letter and  'C' not in letter:
    for i in range(len(letter)):
        letter[i] = 'A'

print(''.join(letter))