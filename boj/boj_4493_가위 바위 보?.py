import sys; sys.stdin = open("4493.txt", "r")

t = int(input())
for i in range(t):
    N = int(input())
    s1, s2 = 0, 0
    for j in range(N):
        p1, p2 = input().split()
        if p1 == 'R':
            if p2 == 'R':
                s1 += 1
                s2 += 1
            elif p2 == 'P':
                s2 += 2
            elif p2 == 'S':
                s1 += 2
        elif p1 == 'P':
            if p2 == 'R':
                s1 += 2
            elif p2 == 'P':
                s1 += 1
                s2 += 1
            elif p2 == 'S':
                s2 += 2
        else:
            if p2 == 'R':
                s2 += 2
            elif p2 == 'P':
                s1 += 2
            elif p2 == 'S':
                s1 += 1
                s2 += 1

    if s1 > s2:
        print("Player 1")
    elif s2 > s1:
        print("Player 2")
    else:
        print("TIE")