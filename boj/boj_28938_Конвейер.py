import sys; sys.stdin = open("28938.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += arr[i]
if ans < 0:
    print("Left")
elif ans > 0:
    print("Right")
else:
    print("Stay")