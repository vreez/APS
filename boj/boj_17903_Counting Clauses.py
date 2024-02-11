import sys; sys.stdin = open("17903.txt", "r")

m, n = map(int, input().split())
for i in range(m):
    arr = list(map(int, input().split()))
if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")
