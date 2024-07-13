import sys; sys.stdin = open("8741.txt", "r")

k = int(input())
num = 2**k - 1
s = num*(num+1)//2
ans = bin(s)[2:]
print(ans)