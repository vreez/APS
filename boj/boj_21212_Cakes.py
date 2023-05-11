import sys; sys.stdin = open("21212.txt", "r")

N = int(input())
check = 100000
for i in range(N):
    need, have = map(int, input().split())
    if have//need < check:
        check = have//need

print(check)