import sys; sys.stdin = open("21955.txt", "r")

N = input()

first = N[:len(N)//2]
second = N[len(N)//2:]
print(first, second)