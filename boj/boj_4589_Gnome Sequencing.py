import sys; sys.stdin = open("4589.txt", "r")

N = int(input())
print("Gnomes:")
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == max(arr):
        if arr[2] == min(arr):
            print("Ordered")
        else:
            print("Unordered")
    elif arr[0] == min(arr):
        if arr[2] == max(arr):
            print("Ordered")
        else:
            print("Unordered")
    else:
        print("Unordered")

