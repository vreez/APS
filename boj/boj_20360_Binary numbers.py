import sys; sys.stdin = open("20360.txt", "r")

N = int(input())
bi = bin(N)
new = str(bi)[2:][::-1]

for i in range(len(new)):
    if new[i] == '1':
        print(i, end=" ")