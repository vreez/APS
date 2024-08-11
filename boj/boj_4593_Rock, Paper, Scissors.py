import sys; sys.stdin = open("4593.txt", "r")

while True:
    first = list(input())
    second = list(input())
    if len(first) == 1 and len(second) == 1 and first[0] == "E" and second[0] == "E":
        break
    else:
        p1 = 0
        p2 = 0
        for i in range(len(first)):
            if first[i] == "R":
                if second[i] == "S":
                    p1 += 1
                elif second[i] == "P":
                    p2 += 1
            elif first[i] == "P":
                if second[i] == "R":
                    p1 += 1
                elif second[i] == "S":
                    p2 += 1
            else:
                if second[i] == "P":
                    p1 += 1
                elif second[i] == "R":
                    p2 += 1
        print("P1: {}".format(p1))
        print("P2: {}".format(p2))

