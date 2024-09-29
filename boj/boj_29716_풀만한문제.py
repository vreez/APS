import sys; sys.stdin = open("29716.txt", "r")

J, N = map(int, input().split())
ans = []
for _ in range(N):
    arr = list(input())
    num = 0
    for i in arr:
        if i.isupper():
            num += 4
        elif i.islower() or i.isdigit():
            num += 2
        elif i == " ":
            num += 1
    ans.append(num)

cnt = 0
for a in ans:
    if a <= J:
        cnt += 1
print(cnt)

