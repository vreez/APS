import sys; sys.stdin = open("783.txt", "r")

first = [1, 2, 3]
second = [2, 4, 6]
third = [3, 6, 9]

print(first + third + third + third + second)