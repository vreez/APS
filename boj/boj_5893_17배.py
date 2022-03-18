import sys; sys.stdin = open("5893.txt", "r")

N = input()
new = int(N, 2)
result = bin(new * 17)[2:]

print(result)