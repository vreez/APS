import sys; sys.stdin = open("743.txt", "r")

first = int(input())
second = int(input())

arr = [first + 1, second - 1, first * (second - 1)]

for i in range(3):
    print(arr[i], end=" ")
