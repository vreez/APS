import sys; sys.stdin = open("30684.txt", "r")

N = int(input())
res = []
for i in range(N):
    name = input()
    if len(name) == 3:
        res.append(name)
new = sorted(res)
print(new[0])