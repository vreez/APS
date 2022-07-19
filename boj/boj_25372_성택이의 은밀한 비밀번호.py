import sys; sys.stdin = open("25372.txt", "r")

N = int(input())
for i in range(N):
    arr = list(input())
    l = len(arr)
    if l >= 6 and l <= 9:
        print("yes")
    else:
        print("no")