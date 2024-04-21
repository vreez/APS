import sys; sys.stdin = open("1703.txt", "r")

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1 and arr[0] == 0:
        break
    else:
        first = arr[0]
        ans = 1
        for i in range(first):
            a = arr[2*i + 1]
            b = arr[2*i + 2]
            ans = ans*a - b
        print(ans)