import sys; sys.stdin = open("11022.txt", "r")

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))
