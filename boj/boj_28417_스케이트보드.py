import sys; sys.stdin = open("28417.txt", "r")

N = int(input())
ans = []
for i in range(N):
    arr = list(map(int, input().split()))
    group1 = arr[:2]
    group2 = arr[2:]
    score1 = max(group1)
    score2 = max(group2)
    group2.remove(score2)
    score2 += max(group2)
    total = score1 + score2
    ans.append(total)
print(max(ans))