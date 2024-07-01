import sys; sys.stdin = open("10874.txt", "r")
N = int(input())
for j in range(N):
    arr = list(map(int, input().split()))
    check = 0
    for i in range(10):
        if arr[i] == (i % 5) + 1:
            check += 1
    if check == 10:
        print(j+1)