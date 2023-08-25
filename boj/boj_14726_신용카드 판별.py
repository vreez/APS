import sys; sys.stdin = open("14726.txt", "r")

N = int(input())
for i in range(N):
    new = list(map(int, input()))
    for j in range(16):
        if j % 2 == 0:
            new[j] = (new[j] * 2)
            if new[j] >= 10:
                new[j] = (new[j] // 10) + (new[j] % 10)
    ans = sum(new)
    if ans % 10 == 0:
        print("T")
    else:
        print("F")
