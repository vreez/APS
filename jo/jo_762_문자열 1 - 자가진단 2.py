import sys; sys.stdin = open("762.txt", "r")

first = input().split()
second = input().split()

print("{} age + {} age = {}".format(first[0], second[0], int(first[1]) + int(second[1])))