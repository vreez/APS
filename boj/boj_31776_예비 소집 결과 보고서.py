import sys; sys.stdin = open("31776.txt", "r")
N = int(input())
ans = 0
for i in range(N):
    t = list(map(int, input().split()))
    if len(set(t)) == 1 and list(set(t))[0] == -1:
        continue
    else:
        for j in range(3):
            if t[j] == -1:
                t[j] = 121
        if t[0] <= t[1] <= t[2]:
            ans += 1

print(ans)


