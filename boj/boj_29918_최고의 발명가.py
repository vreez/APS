import sys; sys.stdin = open("29918.txt", "r")

n, m = map(int, input().split())
mx = 0
for i in range(5):
    a, b = map(int, input().split())
    mx = max(mx, (a-n)+((b-m)*10)+1)
print(mx)