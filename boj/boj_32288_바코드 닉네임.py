import sys; sys.stdin = open("32288.txt", "r")

N = int(input())
S = input()
ans = ""
for i in range(N):
    if S[i] == "I":
        ans += "i"
    else:
        ans += "L"
print(ans)