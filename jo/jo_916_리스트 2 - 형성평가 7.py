n = int(input())
arr = list(map(int, input().split()))
new = sorted(arr, reverse=True)
for i in new:
    print(i)