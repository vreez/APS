import sys; sys.stdin = open("30957.txt", "r")
N = int(input())
ans = [0, 0, 0]
arr = list(input())
for i in range(N):
    if arr[i] == "B":
        ans[0] += 1
    elif arr[i] == "S":
        ans[1] += 1
    else:
        ans[2] += 1

if ans[0] == ans[1] and ans[1] == ans[2]:
    print("SCU")
else:
    if ans.count(max(ans)) == 2:
        if ans[0] == max(ans):
            print("B", end="")
        if ans[1] == max(ans):
            print("S", end="")
        if ans[2] == max(ans):
            print("A", end="")
    else:
        if ans[0] == max(ans):
            print("B", end="")
        elif ans[1] == max(ans):
            print("S", end="")
        else:
            print("A", end="")
