import sys; sys.stdin = open("20254.txt", "r")

Ur, Tr, Uo, To = map(int, input().split())

print(56 * Ur + 24 * Tr + 14 * Uo + 6 * To)