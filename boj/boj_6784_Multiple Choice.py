import sys; sys.stdin = open("6784.txt", "r")

N = int(input())
ans = []
result = 0
for i in range(N):
    num = input()
    ans.append(num)
for i in range(N):
    num = input()
    if ans[i] == num:
        result += 1

print(result)