import sys; sys.stdin = open("2444.txt")

N = int(input())

for i in range(1, N+1):
    answer = ' '*(N-i) + '*'*(2*i-1)
    print(answer)
for i in range(N-1, 0, -1):
    answer = ' '*(N-i) + '*'*(2*i-1)
    print(answer)