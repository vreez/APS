import sys; sys.stdin = open("27239.txt", "r")

arr = []
start = 57
for i in range(8):
    new = []
    for j in range(8):
        new.append(start)
        start += 1
    arr.append(new)
    start -= 16

f = int(input())
for i in range(8):
    for j in range(8):
        if arr[i][j] == f:
            if j == 0:
                print("a{}".format(8-i))
            elif j == 1:
                print("b{}".format(8-i))
            elif j == 2:
                print("c{}".format(8-i))
            elif j == 3:
                print("d{}".format(8-i))
            elif j == 4:
                print("e{}".format(8-i))
            elif j == 5:
                print("f{}".format(8-i))
            elif j == 6:
                print("g{}".format(8-i))
            else:
                print("h{}".format(8-i))