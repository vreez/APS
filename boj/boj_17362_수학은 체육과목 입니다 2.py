import sys; sys.stdin = open("17362.txt", "r")

n = int(input())
ans = (n-1) % 8
if ans == 0:
    print(1)
elif ans == 1 or ans == 7:
    print(2)
elif ans == 2 or ans == 6:
    print(3)
elif ans == 3 or ans == 5:
    print(4)
elif ans == 4:
    print(5)
