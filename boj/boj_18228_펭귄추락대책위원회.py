import sys; sys.stdin = open("18228.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
peng = arr.index(-1)
left = min(arr[:peng])
right = min(arr[peng+1:])
ans = left + right
print(ans)