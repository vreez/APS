import sys; sys.stdin = open("14581.txt", "r")

hj = input()

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(":" + hj + ":", end="")
        else:
            print(":fan:", end="")
    print()