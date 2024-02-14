import sys; sys.stdin = open("31403.txt", "r")

A = input()
B = input()
C = input()

ans1 = int(A) + int(B) - int(C)
ans2 = int(A + B) - int(C)
print(ans1)
print(ans2)