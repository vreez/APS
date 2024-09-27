import sys; sys.stdin = open("26041.txt", "r")

A = list(input().split())
B = input()
ans = 0
for i in A:
    if i != B:
        if i[:len(B)] == B:
            ans += 1
print(ans)

