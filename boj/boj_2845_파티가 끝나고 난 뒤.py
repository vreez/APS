import sys; sys.stdin = open("2845.txt", "r")

a, b = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(5):
    print(arr[i] - (a * b), end=" ")