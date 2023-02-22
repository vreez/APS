import sys; sys.stdin = open("25704.txt", "r")

N = int(input())
P = int(input())

sale = []

if N >= 5:
    sale.append(500)
if N >= 10:
    sale.append(P//10)
if N >= 15:
    sale.append(2000)
if N >= 20:
    sale.append(P//4)

if max(sale) >= P:
    print(0)
else:
    print(P-max(sale))