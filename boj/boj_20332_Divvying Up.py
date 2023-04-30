import sys; sys.stdin = open("20332.txt", "r")

n = int(input())
contest = list(map(int, input().split()))

if sum(contest) % 3:
    print("no")
else:
    print("yes")