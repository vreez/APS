import sys; sys.stdin = open("6779.txt", "r")
h = int(input())
M = int(input())
t = 1
flag = True
while t <= M:
    A = (-6*(t**4) + h*(t**3) + 2*(t**2) + t)
    if A <= 0:
        print("The balloon first touches ground at hour: {}".format(t))
        flag = False
        break
    t += 1
if flag == True:
    print("The balloon does not touch ground in the given time.")