import sys; sys.stdin = open("2446.txt", "r")

N = int(input())

for i in range(N):
    print(i*' ' + ((2*(N-i))-1)*'*')
for i in range(N-2, -1, -1):
    print(i*' ' + ((2*(N-i))-1)*'*')