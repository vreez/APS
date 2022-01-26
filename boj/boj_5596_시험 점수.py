import sys; sys.stdin = open("5596.txt", "r")

minkook = list(map(int, input().split()))
manse = list(map(int, input().split()))

if sum(minkook) > sum(manse):
    print(sum(minkook))
elif sum(manse) > sum(minkook):
    print(sum(manse))
else:
    print(sum(minkook))