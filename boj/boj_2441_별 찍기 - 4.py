import sys; sys.stdin = open("2441.txt", "r")

N = int(input())
for i in range(N):
    answer = ' '*i +'*'*(N-i)
    print(answer)