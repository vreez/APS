import sys; sys.stdin = open("8387.txt", "r")

N = int(input())
first = list(input())
second = list(input())
ans = 0
for i in range(N):
    if first[i] == second[i]:
        ans += 1
print(ans)