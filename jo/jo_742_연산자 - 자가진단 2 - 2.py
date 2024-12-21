import sys; sys.stdin = open("742.txt", "r")

first = int(input())
second = int(input())

arr = []
for i in range(2):
    if i == 0:
        arr.append(first + 100)
    else:
        arr.append(second % 10)

for i in range(2):
    print(arr[i], end=" ")