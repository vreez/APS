import sys; sys.stdin = open("1964.txt", "r")

n = int(input())
ans = 5
num = 7
for i in range(n-1):
    ans += num
    num += 3
print(ans % 45678)

