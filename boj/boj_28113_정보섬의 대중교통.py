import sys; sys.stdin = open("28113.txt", "r")

N, A, B = map(int, input().split())
if A < N + (B-N):
    print("Bus")
elif A > N + (B-N):
    print("Subway")
else:
    print("Anything")