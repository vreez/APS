import sys; sys.stdin = open("2476.txt", "r")

N = int(input())
money = []
for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] and arr[1] == arr[2]:
        result = 10000 + (arr[0] * 1000)
    elif arr[0] == arr[1] and arr[1] != arr[2]:
        result = 1000 + (arr[1] * 100)
    elif arr[0] != arr[1] and arr[1] == arr[2]:
        result = 1000 + (arr[1] * 100)
    elif arr[0] == arr[2] and arr[0] != arr[1]:
        result = 1000 + (arr[2] * 100)
    else:
        result = max(arr) * 100

    money.append(result)

print(max(money))
