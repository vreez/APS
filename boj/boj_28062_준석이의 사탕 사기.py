import sys; sys.stdin = open("28062.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

new = sorted(arr)
total = sum(arr)

if total % 2 == 0:
    print(total)
else:
    for i in range(N):
        if new[i] % 2:
            total -= new[i]
            break
    print(total)