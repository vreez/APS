import sys; sys.stdin = open("30676.txt", "r")

num = int(input())
if num <= 780 and num >= 620:
    print("Red")
elif num < 620 and num >= 590:
    print("Orange")
elif num < 590 and num >= 570:
    print("Yellow")
elif num < 570 and num >= 495:
    print("Green")
elif num < 495 and num >= 450:
    print("Blue")
elif num < 450 and num >= 425:
    print("Indigo")
elif num < 425 and num >= 380:
    print("Violet")