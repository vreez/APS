import sys; sys.stdin = open("1047.txt", "r")

N = int(input())
arr = [1, 1]
for i in range(N-2):
    new = arr[-1] + arr[-2]
    arr.append(new)
print(arr[-1])