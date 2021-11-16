import sys; sys.stdin = open("10102.txt", "r")

N = int(input())
arr = list(input())

A = 0
B = 0

for i in range(N):
    if arr[i] == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print('Tie')
