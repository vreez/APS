import sys; sys.stdin = open("2010.txt", "r")

total = 0
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    com = int(sys.stdin.readline().rstrip())
    total += com
print(total - (N - 1))