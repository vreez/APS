import sys; sys.stdin = open("18408.txt", "r")

arr = list(map(int, input().split()))

one = 0
two = 0

for i in range(3):
    if arr[i] == 1:
        one += 1
    else:
        two += 1

if one > two:
    print(1)
else:
    print(2)