import sys; sys.stdin = open("1920.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

number = {}
for i in range(N):
    number[arr[i]] = 1

for i in range(M):
    if numbers[i] in number:
        print(1)
    else:
        print(0)