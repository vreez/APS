import sys; sys.stdin = open("5751.txt", "r")

while True:
    N = int(input())
    Mary = 0
    John = 0
    if N == 0:
        break
    else:
        arr = list(map(int, input().split()))
        for i in range(N):
            if arr[i] == 0:
                Mary += 1
            else:
                John += 1
    print("Mary won {} times and John won {} times".format(Mary, John))
