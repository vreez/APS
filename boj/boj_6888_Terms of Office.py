import sys; sys.stdin = open("6888.txt", "r")

X = int(input())
Y = int(input())

for i in range(X, Y+1, 60):
    print("All positions change in year {}".format(i))