import sys; sys.stdin = open("2959.txt", "r")

arr = list(map(int, input().split()))
new = sorted(arr)
ans = new[0] * new[2]
print(ans)
