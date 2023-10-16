import sys; sys.stdin = open("29738.txt", "r")

T = int(input())
for i in range(T):
    N = int(input())
    if N > 4500:
        print("Case #{}: {}".format(i+1, "Round 1"))
    elif N > 1000:
        print("Case #{}: {}".format(i + 1, "Round 2"))
    elif N > 25:
        print("Case #{}: {}".format(i + 1, "Round 3"))
    else:
        print("Case #{}: {}".format(i + 1, "World Finals"))