import sys; sys.stdin = open("15814.txt", "r")

S = list(input())
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    imsi = S[A]
    S[A] = S[B]
    S[B] = imsi
print("".join(S))