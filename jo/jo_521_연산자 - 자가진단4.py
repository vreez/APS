import sys; sys.stdin = open("521.txt", "r")

a, b = map(int, input().split())
print(a+1, b-1, a*(b-1))