import sys; sys.stdin = open("14910.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)

if new == arr:
    print("Good")
else:
    print("Bad")
