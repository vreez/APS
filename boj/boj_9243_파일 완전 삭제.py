import sys; sys.stdin = open("9243.txt", "r")

N = int(input())
origin = list(input())
new = list(input())
for i in range(N):
    for j in range(len(origin)):
        if origin[j] == "0":
            origin[j] = "1"
        else:
            origin[j] = "0"
if origin == new:
    print("Deletion succeeded")
else:
    print("Deletion failed")