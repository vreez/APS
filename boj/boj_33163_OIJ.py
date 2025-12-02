N = int(input())
S = input()

ans = ""
for i in range(N):
    if S[i] == "J":
        ans += "O"
    elif S[i] == "O":
        ans += "I"
    else:
        ans += "J"
print(ans)

