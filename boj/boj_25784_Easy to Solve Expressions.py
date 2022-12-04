import sys; sys.stdin = open("25784.txt", "r")

arr = list(map(int, input().split()))

new_arr = sorted(arr)

if new_arr[0] + new_arr[1] == new_arr[2]:
    print(1)
elif new_arr[0] * new_arr[1] == new_arr[2]:
    print(2)
else:
    print(3)
