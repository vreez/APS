import sys; sys.stdin = open("17388.txt", "r")

arr = list(map(int, input().split()))

if sum(arr) >= 100:
    print("OK")
else:
    if min(arr) == arr[0]:
        print("Soongsil")
    elif min(arr) == arr[1]:
        print("Korea")
    else:
        print("Hanyang")
