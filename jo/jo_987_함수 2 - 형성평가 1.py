N = int(input())
arr = list(map(int, input().split()))
new = sorted(arr, reverse=True)
print(" ".join(map(str, new)))
