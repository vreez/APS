import sys; sys.stdin = open("2857.txt", "r")

arr = list(input() for i in range(5))

long = 0
for i in range(5):
    N = len(arr[i])
    if N > long:
        long = N

for i in range(5):
    if len(arr[i]) < long:
        arr[i] = arr[i] + "*" * (long - len(arr[i]))

answer = ""
for i in range(long):
    for j in range(5):
        if arr[j][i] != "*":
            answer += arr[j][i]

print(answer)