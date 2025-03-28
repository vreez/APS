import sys; sys.stdin = open("802.txt", "r")

height = int(input())
weight = int(input())
check = weight + 100 - height
print(check)
if check > 0:
    print("Obesity")