import sys; sys.stdin = open("2774.txt", "r")

T = int(input())
for i in range(T):
    X = list(input())
    new = set(X)
    print(len(new))
    