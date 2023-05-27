import sys; sys.stdin = open("9723.txt", "r")

N = int(input())
for i in range(N):
    tri = list(map(int, input().split()))
    new = sorted(tri)
    if (new[2]**2) == (new[0]**2) + (new[1]**2):
        print("Case #{}: YES".format(i+1))
    else:
        print("Case #{}: NO".format(i+1))