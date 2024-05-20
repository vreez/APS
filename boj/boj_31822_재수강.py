import sys;sys.stdin = open("31822.txt", "r")

cnt = 0
code = input()
N = int(input())
for i in range(N):
    num = input()
    if code[:5] == num[:5]:
        cnt += 1
print(cnt)
