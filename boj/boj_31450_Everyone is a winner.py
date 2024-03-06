import sys; sys.stdin = open("31450.txt", "r")

M, K = map(int, input().split())
if M % K == 0:
    print("Yes")
else:
    print("No")