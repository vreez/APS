import sys; sys.stdin = open("5054.txt", "r")

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    new = sorted(arr)
    total = new[-1] - new[0]
    for j in range(1, len(new)):
        total += new[j] - new[j-1]
    print(total)
