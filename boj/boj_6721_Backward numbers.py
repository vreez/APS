import sys; sys.stdin = open("6721.txt", "r")

N = int(input())
for i in range(N):
    a, b = input().split()
    ans = int(str(int(a[::-1]) + int(b[::-1]))[::-1])
    print(ans)