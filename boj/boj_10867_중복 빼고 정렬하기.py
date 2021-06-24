import sys; sys.stdin = open("10867.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

minus = []
plus = []

for i in range(len(arr)):
    if arr[i] < 0:
        minus.append(arr[i])
    else:
        plus.append(arr[i])

sorted_minus = list(set(minus))
sorted_plus = list(set(plus))

sorted_minus.sort()
sorted_plus.sort()

total = sorted_minus + sorted_plus

for i in range(len(total)):
    print(total[i], end=' ')