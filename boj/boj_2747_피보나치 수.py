import sys; sys.stdin = open("2747.txt", "r")

N = int(input())

arr = [0, 1]
for i in range(N):
    arr.append(arr[-1] + arr[-2])
print(arr[N])