import sys; sys.stdin = open("9635.txt", "r")

T = int(input())
for i in range(T):
    N, X, Y = map(int, input().split())
    arr = list(map(int, input().split()))
    if arr[0] == X and arr[-1] == Y:
        print("BOTH")
    elif arr[0] == X:
        print("EASY")
    elif arr[-1] == Y:
        print("HARD")
    else:
        print("OKAY")