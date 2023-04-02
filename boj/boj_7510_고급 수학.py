import sys; sys.stdin = open("7510.txt", "r")

N = int(input())
for i in range(1, N+1):
    print("Scenario #{}:".format(i))
    arr = list(map(int, input().split()))
    new = sorted(arr)
    if (new[0])*(new[0]) + (new[1])*(new[1]) == (new[2])*(new[2]):
        print("yes")
    else:
        print("no")
    print()