import sys; sys.stdin = open("2439.txt", "r")

N = int(input())

arr = [[" "] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i >= N-1-j:
            arr[i][j] = '*'

# sep : 문자 사이 공백에 어떤 문자를 넣을 지 정할 때 사용
for i in arr:
    print(*i, sep="")