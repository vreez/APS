import sys; sys.stdin = open("26531.txt", "r")

arr = list(input().split())
if int(arr[0]) + int(arr[2]) == int(arr[4]):
    print("YES")
else:
    print("NO")