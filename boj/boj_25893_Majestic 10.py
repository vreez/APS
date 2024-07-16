import sys; sys.stdin = open("25893.txt", "r")

check = ["zilch", "double", "double-double", "triple-double"]
N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    cnt = 0
    for j in range(3):
        if arr[j] >= 10:
            cnt += 1
    print(arr[0], arr[1], arr[2])
    print(check[cnt])
    print()