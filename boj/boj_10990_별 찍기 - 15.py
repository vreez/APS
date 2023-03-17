import sys; sys.stdin = open("10990.txt", "r")

N = int(input())
print(" "*(N-1) + "*")
for i in range(1, N):
    print((" " * (N-i-1)) + "* " + (" " * ((i-1)*2)) + "*")