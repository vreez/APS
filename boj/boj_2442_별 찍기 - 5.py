import sys; sys.stdin = open("2442.txt", "r")

N = int(input())

for i in range(N):
    answer = ' ' * (N-(i+1)) + '*'*(2*(i+1)-1)
    print(answer)
