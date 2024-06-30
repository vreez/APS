import sys; sys.stdin = open("1392.txt", "r")

N, Q = map(int, input().split())
li = []
for i in range(1, N+1):
    num = int(input())
    li += ([i]*num)

for j in range(Q):
    id = int(input())
    print(li[id])