import sys; sys.stdin = open("24937.txt", "r")

N = int(input())
cha = "SciComLove"
for i in range(N%10):
    cha = cha[1:] + cha[0]
print(cha)