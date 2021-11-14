import sys; sys.stdin = open("17350.txt", "r")

N = int(input())
check = False
for _ in range(N):
    word = input()
    if word == 'anj':
        check = True
        break

if check == True:
    print('뭐야;')
else:
    print('뭐야?')
