import sys; sys.stdin = open("32184.txt", "r")

A, B = map(int, input().split())
if A % 2 == 0 and B % 2 != 0:
    ans = (B-A)//2 + 2
else:
    ans = (B-A)//2 + 1
print(ans)