import sys; sys.stdin = open("8901.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    AB, BC, CA = map(int, input().split())
    big = 0
    # AB의 개수를 기준으로 두고, 나머지 것들의 개수를 구하는 것이 관건!
    for i in range(min(A, B)+1):
        total = 0
        if BC >= CA:
            total += (AB * i) + (BC * min(C, (B - i))) + (CA * min((A - i), (C - min(C, (B - i)))))
        else:
            total += (AB * i) + (CA * min(C, (A - i))) + (BC * min((B - i), (C - min(C, (A - i)))))

        if total >= big:
            big = total

    print(big)