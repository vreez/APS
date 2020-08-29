import sys
sys.stdin = open("2805.txt")


T = int(input())
for tc in range(1, T+1):
    t = int(input())
    arr = [list(map(int, list(input()))) for _ in range(t)]

    total = 0

    s, e = t//2, t//2
    for i in range(t):
        if i < t//2:
            for j in range(s, e + 1):
                total += arr[i][j]
            s -= 1
            e += 1
        elif i == t//2:
            for j in range(s, e + 1):
                total += arr[i][j]
            s += 1
            e -= 1
        else:
            for j in range(s, e + 1):
                total += arr[i][j]
            s += 1
            e -= 1

    print("#{} {}".format(tc, total))




