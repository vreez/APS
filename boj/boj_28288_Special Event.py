import sys; sys.stdin = open("28288.txt", "r")

N = int(input())
check = [0]*5
for i in range(N):
    arr = list(input())
    for j in range(5):
        if arr[j] == "Y":
            check[j] += 1
ans = []
for k in range(5):
    if check[k] == max(check):
        ans.append(k+1)

for l in range(len(ans)):
    print(ans[l],end="")
    if l+1 < len(ans):
        print(",",end="")

