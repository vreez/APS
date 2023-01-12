import sys; sys.stdin = open("25932.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    if 17 in arr and 18 in arr:
        print(' '.join(map(str, arr)))
        print("both")
        print()
    elif 17 in arr and 18 not in arr:
        print(' '.join(map(str, arr)))
        print("zack")
        print()
    elif 18 in arr and 17 not in arr:
        print(' '.join(map(str, arr)))
        print("mack")
        print()
    else:
        print(' '.join(map(str, arr)))
        print("none")
        print()