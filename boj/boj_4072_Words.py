import sys; sys.stdin = open("4072.txt", "r")

while True:
    arr = list(input().split())
    if len(arr) == 1 and arr[0] == "#":
        break
    else:
        for i in range(len(arr)):
            new = arr[i][::-1]
            print(new, end=" ")
        print()