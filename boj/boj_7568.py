import sys; sys.stdin = open("7568.txt", "r")

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

result = [1] * T

for i in range(T):
    for j in range(T):
        if i != j:
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                result[i] += 1

for i in range(T):
    print(result[i], end=" ")
