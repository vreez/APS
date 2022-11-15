import sys; sys.stdin = open("21964.txt", "r")

N = int(input())
S = list(input())
new = S[N-5:]
print("".join(new))