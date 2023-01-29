import sys; sys.stdin = open("5356.txt", "r")
from string import ascii_uppercase

alpha = list(ascii_uppercase)

N = int(input())
for i in range(N):
    num, word = input().split()
    new = ord(word)
    for j in range(int(num)):
        if new + j >= 91:
            new -= 26
        print(chr(new+j) * (j+1))
    print()
