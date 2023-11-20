import sys; sys.stdin = open("30501.txt", "r")

N = int(input())
for i in range(N):
    name = list(input())
    if 'S' in name:
        print("".join(name))
        break
