import sys; sys.stdin = open("17094.txt", "r")

N = int(input())
arr = list(input())
num = 0
word = 0
for i in range(N):
    if arr[i] == '2':
        num += 1
    else:
        word += 1

if num > word:
    print(2)
elif word > num:
    print('e')
else:
    print('yee')