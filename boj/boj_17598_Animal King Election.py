import sys; sys.stdin = open("17598.txt", "r")

L = 0
T = 0
for i in range(9):
    vote = input()
    if vote == "Lion":
        L += 1
    else:
        T += 1

if L > T:
    print("Lion")
else:
    print("Tiger")
