import sys; sys.stdin = open("2588.txt", "r")

A = int(input())
B = int(input())
strB = list(str(B))

print(A * int(strB[2]))
print(A * int(strB[1]))
print(A * int(strB[0]))
print(A * B)