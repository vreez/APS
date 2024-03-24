import sys; sys.stdin = open("31616.txt", "r")

S = int(input())
N = list(input())
new = set(N)
if len(new) == 1:
    print("Yes")
else:
    print("No")