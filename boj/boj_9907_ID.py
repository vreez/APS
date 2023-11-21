import sys; sys.stdin = open("9907.txt", "r")

N = list(input())
total = 0
for i in range(7):
    if i == 0:
        total += int(N[i]) * 2
    elif i == 1:
        total += int(N[i]) * 7
    elif i == 2:
        total += int(N[i]) * 6
    elif i == 3:
        total += int(N[i]) * 5
    elif i == 4:
        total += int(N[i]) * 4
    elif i == 5:
        total += int(N[i]) * 3
    else:
        total += int(N[i]) * 2
result = total % 11
if result == 0:
    print("J")
elif result == 1:
    print("A")
elif result == 2:
    print("B")
elif result == 3:
    print("C")
elif result == 4:
    print("D")
elif result == 5:
    print("E")
elif result == 6:
    print("F")
elif result == 7:
    print("G")
elif result == 8:
    print("H")
elif result == 9:
    print("I")
else:
    print("Z")