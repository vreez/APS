import sys; sys.stdin  = open("28691.txt", "r")

letter = input()
if letter == "M":
    print("MatKor")
elif letter == "W":
    print("WiCys")
elif letter == "C":
    print("CyKor")
elif letter == "A":
    print("AlKor")
else:
    print("$clear")