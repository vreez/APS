import sys; sys.stdin = open("8958.txt", "r")

N = int(input())
for _ in range(N):
    arr = list(input())
    count = 0
    total = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)
