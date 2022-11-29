import sys; sys.stdin = open("26082.txt", "r")

A, B, C = map(int, input().split())
print(B // A  * 3 * C)