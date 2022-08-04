import sys; sys.stdin = open("18698.txt", "r")

T = int(input())
for i in range(T):
    arr = list(input())
    count = 0
    for i in range(len(arr)):
        if arr[i] != "D":
            count += 1
        else:
            break

    print(count)