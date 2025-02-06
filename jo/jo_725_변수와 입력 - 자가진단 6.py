import sys; sys.stdin = open("725.txt", "r")

first = int(input())
second = int(input())

print("Number 1? Number 2?", end=" ")
print("{} * {} = {}".format(first, second, first * second))
print("{} / {} = {}".format(first, second, first / second))