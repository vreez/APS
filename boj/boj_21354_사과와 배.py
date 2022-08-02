import sys; sys.stdin = open("21354.txt", "r")

A, P = map(int, input().split())

if A * 7 > P * 13:
    print("Axel")
elif A * 7 < P * 13:
    print("Petra")
else:
    print("lika")