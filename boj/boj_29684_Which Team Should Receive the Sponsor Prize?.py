import sys; sys.stdin = open("29684.txt", "r")

while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = list(map(int, input().split()))
        new = []
        for i in range(N):
            new.append(abs(arr[i]-2023))
        minNum = min(new)
        for i in range(N):
            if new[i] == minNum:
                print(i+1)