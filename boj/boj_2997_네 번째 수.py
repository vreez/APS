import sys; sys.stdin = open("2997.txt", "r")

arr = list(map(int, input().split()))
new_arr = sorted(arr)
a = new_arr[1] - new_arr[0]
b = new_arr[2] - new_arr[1]

if a == b:
    print(new_arr[2] + b)
elif a > b:
    print(new_arr[0] + b)
else:
    print(new_arr[2] - a)