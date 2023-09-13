import sys; sys.stdin = open("2920.txt", "r")

arr = list(map(int, input().split()))
check = ""
count = 0
asc = sorted(arr)
desc = sorted(arr)[::-1]

if arr == asc:
    print("ascending")
elif arr == desc:
    print("descending")
else:
    print("mixed")
