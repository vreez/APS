import sys; sys.stdin = open("11650.txt", "r")

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x:(x[0], x[1]))
for i in range(N):
    print(arr[i][0], arr[i][1])

