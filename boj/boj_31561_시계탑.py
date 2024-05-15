import sys; sys.stdin = open("31561.txt", "r")

M = int(input())
ans = 0
if M >= 30:
    ans += 15
    M -= 30
    ans += (M * 1.5)
else:
    ans = M / 2
print("{:.1f}".format(ans))