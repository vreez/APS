import sys; sys.stdin = open("6768.txt", "r")

J = int(input())

print((J-1) * (J-2) * (J-3) // (3 * 2 * 1))
