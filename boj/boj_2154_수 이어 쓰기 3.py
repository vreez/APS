import sys; sys.stdin = open("2154.txt", "r")

N = int(input())
num = ""
for i in range(1, N+1):
    num += str(i)

print(num.find(str(N))+1)