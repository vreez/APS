import sys; sys.stdin = open("27213.txt", "r")
m = int(input())
n = int(input())
if m == 1 or n == 1:
    ans = m + n - 1
else:
    ans = (m + n) * 2 - 4
print(ans)