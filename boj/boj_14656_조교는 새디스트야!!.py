import sys; sys.stdin = open("14656.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
new_arr = sorted(arr)

answer = 0
for i in range(N):
    if arr[i] != new_arr[i]:
        answer += 1

print(answer)