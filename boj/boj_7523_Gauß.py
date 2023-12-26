import sys; sys.stdin = open("7523.txt", "r")

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    if n > 0:
        total = (m*(m+1)//2) - (n*(n+1)//2) + n
    else:
        total = (m*(m+1)//2) - (-n*(-n+1)//2)

    print("Scenario #{}:".format(i+1))
    print(total)
    print()