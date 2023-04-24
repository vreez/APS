import sys; sys.stdin = open("27329.txt", "r")

N = int(input())
S = input()
if S[:N//2] == S[N//2:]:
    print("Yes")
else:
    print("No")