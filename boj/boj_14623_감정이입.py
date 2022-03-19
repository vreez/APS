import sys; sys.stdin = open("14623.txt", "r")

B1 = int(input(), 2)
B2 = int(input(), 2)

result = bin(B1 * B2)[2:]
print(result)