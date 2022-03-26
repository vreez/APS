import sys; sys.stdin = open("21300.txt", "r")

arr = list(map(int, input().split()))
answer = 0
for i in range(len(arr)):
    answer += (arr[i] * 5)
print(answer)