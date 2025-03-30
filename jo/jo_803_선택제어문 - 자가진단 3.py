import sys; sys.stdin = open("803.txt", "r")

age = int(input())
if age >= 20:
    print("An adult.")
else:
    print("{} years".format(20 - age))