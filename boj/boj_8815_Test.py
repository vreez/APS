import sys; sys.stdin = open("8815.txt", "r")

alpha = ["A", "B", "C", "B", "C", "D", "C", "D", "A", "D", "A", "B"]

N = int(input())
for i in range(N):
    num = int(input())
    print(alpha[num % 12-1])

