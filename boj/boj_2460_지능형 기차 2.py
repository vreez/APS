import sys; sys.stdin = open("2460.txt", "r")

nums = 0
big = 0
for i in range(10):
    O, I = map(int, input().split())
    nums -= O
    nums += I
    if nums > big:
        big = nums

print(big)
