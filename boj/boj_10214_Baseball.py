import sys; sys.stdin = open("10214.txt", "r")

T = int(input())
for _ in range(T):
    yon = 0
    ko = 0
    for _ in range(9):
        y, k = map(int, input().split())
        yon += y
        ko += k
    if yon > ko:
        print("Yonsei")
    elif ko > yon:
        print("Korea")
    else:
        print("Draw")