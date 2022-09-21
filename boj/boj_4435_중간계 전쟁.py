import sys; sys.stdin = open("4435.txt", "r")

N = int(input())
for i in range(N):
    print("Battle {}:".format(i+1), end=" ")
    G = list(map(int, input().split()))
    GT = (G[0]*1) + (G[1]*2) + (G[2]*3) + (G[3]*3) + (G[4]*4) + (G[5]*10)
    S = list(map(int, input().split()))
    ST = (S[0]*1) + (S[1]*2) + (S[2]*2) + (S[3]*2) + (S[4]*3) + (S[5]*5) + (S[6]*10)
    if GT == ST:
        print("No victor on this battle field")
    elif GT > ST:
        print("Good triumphs over Evil")
    else:
        print("Evil eradicates all trace of Good")
