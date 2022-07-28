import sys; sys.stdin = open("13580.txt", "r")

arr = list(map(int, input().split()))

arr = sorted(arr)
new_set = set(arr)
new_list = list(new_set)
n = len(new_list)

if n == 2 or n == 1:
    print("S")
elif arr[0] + arr[1] == arr[2]:
    print("S")
else:
    print("N")
