import sys; sys.stdin = open("1267.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

a = 0
b = 0
for i in range(N):
    a += ((arr[i] // 30) + 1) * 10
    b += ((arr[i] // 60) + 1) * 15

if a < b:
    print("Y", a)
elif b < a:
    print("M", b)
else:
    print("Y M", a)