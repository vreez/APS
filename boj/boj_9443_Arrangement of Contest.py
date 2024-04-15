import sys; sys.stdin = open("9443.txt", "r")

N = int(input())
alpha = []
for i in range(N):
    text = input()
    alpha.append(text[0])
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
while ans < 26:
    if al[ans] not in alpha:
        break
    else:
        ans += 1
print(ans)