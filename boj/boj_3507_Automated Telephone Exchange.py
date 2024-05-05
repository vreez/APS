import sys; sys.stdin = open("3507.txt", "r")

N = int(input())
if N > 198:
    print(0)
else:
    print(199-N)