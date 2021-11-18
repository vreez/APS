import sys; sys.stdin = open("5598.txt", "r")

before = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
          'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
          'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          ]
after = [
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'A', 'B', 'C'
    ]

word = list(input())
answer = ''
for i in range(len(word)):
    answer += before[after.index(word[i])]

print(answer)

