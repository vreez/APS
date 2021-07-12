import sys; sys.stdin = open("input/12847.txt", "r")

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

profit = 0
count = 0
maxSum = 0
for i in range(N):
    profit += arr[i]
    # M일을 초과할 경우
    if i >= M - 1:
        maxSum = max(maxSum, profit)
        # 항상 M일 간의 일급만 받을 수 있으므로,
        # 총합에 새롭게 하나의 일급을 더하는 만큼 가장 처음 받은 일급을 총합에서 빼준다.
        profit -= arr[count]
        count += 1

print(maxSum)