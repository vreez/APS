import sys; sys.stdin = open("13410.txt", "r")

N, K = map(int, input().split())
arr = []
for i in range(1, K+1):
    num = N * i
    new = int(str(num)[::-1])
    arr.append(new)

print(max(arr))