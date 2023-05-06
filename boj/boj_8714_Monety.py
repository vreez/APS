import sys; sys.stdin = open("8714.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

one = arr.count(1)
zero = arr.count(0)

if one >= zero:
    print(zero)
else:
    print(one)