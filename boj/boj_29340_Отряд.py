import sys; sys.stdin = open("29340.txt", "r")

a = input()
b = input()
ans = ""
for i in range(len(a)):
    if a[i] >= b[i]:
        ans += a[i]
    else:
        ans += b[i]
print(int(ans))
