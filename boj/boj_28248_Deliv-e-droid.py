import sys; sys.stdin = open("28248.txt", "r")

G = int(input())
L = int(input())
total = 0
total += (G*50)
total -= (L*10)
if G > L:
    total += 500

print(total)
