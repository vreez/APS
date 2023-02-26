import sys; sys.stdin = open("27541.txt", "r")

N = int(input())
S = list(input())

if S[-1] == "G":
    S = S[:-1]
    print(''.join(S))
else:
    S.append("G")
    print(''.join(S))