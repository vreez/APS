import sys; sys.stdin = open("6887.txt", "r")

N = int(input())

leng = int(N ** (1/2))
print("The largest square has side length {}.".format(leng))