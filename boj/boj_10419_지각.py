import sys; sys.stdin = open("10419.txt", "r")

T = int(input())
for _ in range(T):
    d = int(input())
    ans = 0
    for i in range(d):
        if (i + (i*i)) <= d:
            ans = i
    print(ans)