n = int(input())
alpha = "0abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in range(len(alpha)):
    if n == 1:
        ans = "abcdefghijklmnopqrstuvwxyz"
    else:
        if alpha.index(alpha[i]) % n == 0:
            if alpha.index((alpha[i])) != 0:
                ans += alpha[i]
print(ans)