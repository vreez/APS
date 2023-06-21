import sys; sys.stdin = open("17210.txt", "r")

N = int(input())
first = int(input())
if N >= 6:
    print("Love is open door")
else:
    for i in range(N):
        if i > 0:
            print(first)
        if first == 0:
            first = 1
        else:
            first = 0